"""
Flask server for running evals
"""

from flask import Flask, jsonify, request
from flask_cors import CORS
# from langdrive import LangDrive
from run_eval import Eval

import os

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    try:
        response = {"response": True}
        return jsonify(response), 200
    
    except Exception as e:
        error = str(e)
        app.logger.error(str(e))
        return jsonify({"error": "Internal server error", "message": error}), 500
    

@app.route('/eval', methods=['POST'])
def evaluate():
    try:
    
        # Get the required attributes from the request body
        data = request.json["data"]

        chunks = data["chunks"]
        if len(chunks) <= 1:
            raise ValueError("ChunkLengthMustBeMoreThanOne")
        
        # For all chunks, get the eval
        evaluation = Eval()
        cosine_similarities = []

        for i in range(len(chunks)):
            if i == 0:
                # Compare first chunk with the next one
                print(f"Compare chunk {i} with chunk{i+1}")
                current_chunk = chunks[i]["chunk"]
                next_chunk = chunks[i+1]["chunk"]
                cosine_similarity = evaluation.cosine_simililarity_between_two_texts(current_chunk, next_chunk)
                cosine_similarities.append(cosine_similarity)

            elif i == len(chunks) - 1:
                # Compare last element with the one before
                print(f"Compare chunk {i} with chunk{i-1}")
                prev_chunk = chunks[i-1]["chunk"]
                current_chunk = chunks[i]["chunk"]
                cosine_similarity = evaluation.cosine_simililarity_between_two_texts(current_chunk, prev_chunk)
                cosine_similarities.append(cosine_similarity)
            else:
                # Compare middle chunks with the previous and next chunks
                print(f"Compare chunk{i} with chunks[{i-1} and chunk{i+1}")
                prev_chunk = chunks[i-1]["chunk"]
                next_chunk = chunks[i+1]["chunk"]
                current_chunk = chunks[i]["chunk"]
                cosine_similarity_1 = evaluation.cosine_simililarity_between_two_texts(current_chunk, next_chunk)
                cosine_similarity_2 = evaluation.cosine_simililarity_between_two_texts(current_chunk, prev_chunk)
                cosine_similarities.append(cosine_similarity_1)
                cosine_similarities.append(cosine_similarity_2)

        # Get the average cosine similarity
        average_cosine_similarity = sum(cosine_similarities) / len(cosine_similarities)

        # Return response
        return jsonify({"average_cosine_similarity": average_cosine_similarity,
                        "success": True}), 200
    except Exception as e:
        app.logger.error(str(e))
        return jsonify({"error": "Internal server error"}), 500


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
