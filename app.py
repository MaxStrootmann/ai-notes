import os
import random
from flask import Flask, flash, jsonify, redirect, render_template, request, session

# Configure application
app = Flask(__name__)

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route('/', methods=['POST'])
def upload_audio():
    # Check if the 'audio_file' is part of the request
    if 'audio_file' not in request.files:
        return {'error': 'No file part'}, 400
    
    file = request.files['audio_file']
    
    # Check if the user uploaded an actual file
    if file.filename == '':
        return {'error': 'No selected file'}, 400
    
    if file and file.filename:
        # Save the file to the uploads folder
        n = random.randint(0, 10)
        file_path = "./" + str(n) + file.filename
        file.save(file_path)
        return {'message': 'File uploaded successfully', 'file_path': file_path}, 200
    
    return jsonify({'status': 'received, not handled'}), 200
