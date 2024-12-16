import logging
import json
from flask import Flask, request, jsonify, send_file
from werkzeug.middleware.proxy_fix import ProxyFix
from services.email_service import send_email
from services.pyannote_service import diarize

# 16-dec, works with cmd: curl -v -X POST -F "audio_file=@/home/max/ai-notes/2dekamer.mp3" https://dbln.nl
# prints to gunicorn_error.log and emails the diarization json


app = Flask(__name__)
app.wsgi_app = ProxyFix(
    app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1
)

if __name__ != '__main__':
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)

@app.route('/', methods=['POST'])
def handle_recording():
        # Check if the 'audio_file' is part of the request
    if 'audio_file' not in request.files:
        return {'error': 'No file part'}, 400

    file = request.files['audio_file']

    # Check if the user uploaded an actual file
    if file.filename == '':
        return {'error': 'No selected file'}, 400

    if file and file.filename:
        # Save the file to the uploads folder
        file_path = "./" + file.filename
        file.save(file_path)
        file_url = f"https://dbln.nl/get-url//{file.filename}"
        app.logger.info(f"Upload successful, path: {file_path}, url: {file_url}")
        diarize(file_url)

        return jsonify({'status': 'received'}), 200

    # delete file from disk

    return jsonify({'status': 'received, not handled'}), 200


@app.route('/get-url/<path:file_path>', methods=['GET'])
def get_audio_file(file_path):
    print(f"file_path: {file_path}")
    return send_file(file_path, mimetype='audio/mpeg')


@app.route('/pyannote-webhook', methods=['POST'])
def handle_webhook():
    app.logger.info(f"Webhook received")
    data = request.json
    app.logger.info(f"Received data: {data}")
    json_str = json.dumps(data, indent=4)
    send_email(json_str)
    return jsonify({'status': 'received'}), 200
