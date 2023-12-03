"""
Flask server for running evals
"""

from flask import Flask, jsonify, request
from flask_cors import CORS
import requests
# from lan  gdrive import LangDrive
from run_eval import Eval
import json
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
    

@app.route("/batch")
def batch():
    try:
        # Get the directory path where the batch outputs are
        folder_path = request.args.get('folder_path')
        directory_path = f"../{folder_path}"
        data = {}

        final_response = []
        for filename in os.listdir(directory_path):
            # Check if file is a .json file
            if filename.endswith(".json"):
                file_path = os.path.join(directory_path, filename)

                # Open the file and load it as JSON
                with open(file_path, 'r') as f:
                    file_data = json.load(f)
                
                # Add the data from this file to main data object
                print(type(file_data))
                url = 'http://127.0.0.1:8080/eval'

                # Define the data you want to send as post
                headers = {'Content-Type': 'application/json'}
                data = {
                    "data": file_data
                }

                # Send the POST request
                response = requests.post(url, headers=headers, data=json.dumps(data))

                # Add average_cosine_similarity to file_data and write into file
                file_data["average_cosine_similarity"] = response.json()["average_cosine_similarity"]
                with open(file_path, 'w') as f:
                    json.dump(file_data, f)


                final_response.append({
                    "filename": filename,
                    "average_cosine_similarity": response.json()["average_cosine_similarity"]
                })
                print(response.json())


        return jsonify({"response": final_response,
                        "success": True}), 200


    
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
