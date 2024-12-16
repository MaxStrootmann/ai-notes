import os
import requests

def diarize(file_url):
    # Access the variables
    API_KEY = os.getenv("PYANNOTE_API_KEY")
    
    url = "https://api.pyannote.ai/v1/diarize"
    file_url = file_url
    webhook_url = 'https://dbln.nl/pyannote-webhook'
    headers = {
        "Authorization": f"Bearer {API_KEY}"
    }
    data = {
        'webhook': webhook_url,
        'url': file_url
    }
    response = requests.post(url, headers=headers, json=data)
    
    print(response.status_code)
    # 200
    print(response.json()) 
    # {
    #  "jobId": "bd7e97c9-0742-4a19-bd5a-9df519ce8c74",
    #  "message": "Job added to queue",
    #  "status": "pending"
    # }


if __name__ == "__main__":
    diarize("/home/max/ai-notes/2dekamer.mp3")
