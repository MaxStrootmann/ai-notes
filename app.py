import logging
from flask import Flask, request, jsonify, send_file
from werkzeug.middleware.proxy_fix import ProxyFix
from services.email_service import send_email
from services.pyannote_service import diarize


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
    # Write file from request to disk
    # for now use test file
    # is this filepath correct?
    file_path = "/2dekamer.mp3"
    file_url = f"https://dbln.nl/get-url/{file_path}"
    diarize(file_url)

    # Delete file from disk

    return jsonify({"status": "received"}), 200


@app.route('/get-url/<path:file_path>', methods=['GET'])
def get_audio_file(file_path):
    print(f"file_path: {file_path}")
    return send_file(file_path, mimetype='audio/mpeg')


@app.route('/pyannote-webhook', methods=['POST'])
def handle_webhook():
    app.logger.info(f"Webhook received")
    data = request.json
    app.logger.info(f"Received data: {data}")
    send_email(data)
    return jsonify({'status': 'received'}), 200
