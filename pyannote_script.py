from dotenv import load_dotenv
import os
import requests
import resend


def diarize():
    # Load environment variables from .env file
    load_dotenv()
    
    # Access the variables
    API_KEY = os.getenv("PYANNOTE_API_KEY")
    
    url = "https://api.pyannote.ai/v1/diarize"
    file_url = 'https://call-recordings-android.s3.eu-west-1.amazonaws.com/2dekamer.mp3?response-content-disposition=inline&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCWV1LXdlc3QtMSJGMEQCIHmfGoTK%2FlZdGAXZxVNh0RRVcLEXVIes82%2BLMD4pDIsyAiB0hiKgCfLY2QwYhqU64jMyY3BQPZBLNTjCUgWZWZfuhirkAwgTEAAaDDA2MTA1MTI0OTkzNiIMQtb9xOwqFJQxVeltKsEDVpuRznS5X43rNq8sSs5Lg7IeM4qTeb0zffZBEjy1CYxo3n7Jj4D6UmVV%2B7nqhbHOUJzZIJ1wCn6B1PN%2F201f4bnIWrJX634wJhEyMdq1N%2Bd%2BK8qlrD8oEu92BXOAPJjBg2ks0SmewsXIhkoEHP2fQCw5g0PhE9jpPtKRHZZcUedaLl8x%2F2jt0zTWNnrR23XgheUkYGWJr0HuVj0scjm3uzoIwxKSVTuwGM86sztIyXq92H5LpmMrzkIlXJQdZCU7zEtB%2BIf4fw%2FLy8%2F%2Bc2bXgFWW1ANkNMfMVeJCyR6%2BPihgvwjq5LyeZ%2BXbTFokPYb5VGEVGo5p6Bs7Qz9pnhtDlc%2BzSRI60yeUEVC8DzvDOSgvjoHpe709qEVXLO2CE9BxUWz5LGofDYVTuwj49PkuslgJbkpGhpG6LDAIMR2piycIc%2Bt%2FUOcWyXH9fJMgheqoL6nGLZaUrj4d8GtAoqi%2FRPsQuZuWXgxdtO1k60pbbmtJu2yibtSJ1HYiQhIdtujkiLpTyDtHYptjNvBCIL7oCpT%2FRQ7lrhyDjMuU42KBZ3j6zvX6YVCCnTTaZKrrBLjxpiADqL0N4rmJcwYlW6RAC8Uwi8T6ugY65QKHhiCATBWEZoqXxFIF3z1puw%2BNP6nKK2tsmccxFgJvknktL%2B43lv9aiaFX2J0zr0t3V62Wsf2ZQSd8Yi25Fc%2Fid%2FE7Pdbhkfh3gwlyRw7RtCp1DDVa3lHlVhvgXvirRu9D59atj%2BjCapcoCZsCsqYdt7QqCdVB1zIflZu2KZaT310zwWdutJvlPCSsyaYMcuNPU1jGzop1SCogFo9hRBUrMUFYLImSDjwUj89On0stzwNlE7IgRLWdU33SuOOw1yH60ttPgh8aAHXVSEZs2KDaQoxBkncV%2BVqjOE1%2BByihz66RPj6mf1%2FarmRls22eu917peqt4tNJ%2FQN4LWo%2FveByxIL4BtMXPJwoogJu4QfLC4yLYy0F35oVFkkUiAEbBSUYiFrdu1s3nWDPQxcMTL%2BdYt6z2KfFupDTchGL%2FzC8ouXDwi1zDbl8h0f9WHsqVi2s4QWsq0VjsZo15JaZ8S5GD3eTh%2B8%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ASIAQ4NXQEUIBICU64WH%2F20241215%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20241215T093338Z&X-Amz-Expires=43200&X-Amz-SignedHeaders=host&X-Amz-Signature=7cb800c45fc73c8de3b87702f9fbaee954492c250375b37ea4ec9e26d23f7a92'
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
    diarize()
