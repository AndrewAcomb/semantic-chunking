"""
Hello
"""

from flask import Flask, jsonify, request
from flask_cors import CORS

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
    

@app.route('/train', methods=['POST'])
def completion():
    try:
    
        # Get the required attributes from the request body
        chunks = request.json["chunks"]
        document = request.json["document"]
       
        # For all chunks, get the eval
        for chunk in chunks:
            chunk_text = chunk["chunk"]
            original_text = chunk["original_text"]
            # Get file content

            # Get expected value
            
        
        response = vertex_ai.make_completion(messages)
        if not response:
            raise ValueError("ResponseUndefined")

        # Return response
        return jsonify({"response": response,
                        "success": True}), 200
    except Exception as e:
        app.logger.error(str(e))
        return jsonify({"error": "Internal server error"}), 500


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
