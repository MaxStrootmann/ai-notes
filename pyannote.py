import os
import requests

API_KEY = os.environ["PYANNOTE_API_KEY"]

url = "https://api.pyannote.ai/v1/diarize"
file_url = 'https://call-recordings-android.s3.eu-west-1.amazonaws.com/2dekamer.mp3?response-content-disposition=inline&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCWV1LXdlc3QtMSJIMEYCIQCrSXXSGLknAwduiEi2n%2B6kk6nk5YI1jfbe3shDEExj%2FAIhALUMQ8fq%2B8GftBiCweSnG3b8fyKy22EySNs40BulgJxYKu0DCMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMMDYxMDUxMjQ5OTM2IgzLPZIkzgEd%2F59qOIsqwQPWqTyagQZQ1CDtzN0XbNzAWtp9pc0DQE%2BdPi2A1YOoxqzrXjmrBk7UNdt0M%2FRZ1WjrfY48SOmi4ilHcUpKRNAk6%2FfmntKzHp8MMIppQTe93Qd2BEFox1LTtl8%2BSk6Qqf3GIvEIAlHKsO8eXsyF2HyDhlMnjBE0AyYw%2FI9EzJKcvG3tWodJaJU7myyRL9DCRF6O5FOrvwGu8Tuh5fEuNxWHcZi4x2p1252Ezt0BjbofBmViS6yD9hldQqenlINLYIqFFw5XnCJ2N4GVd1YkfsOuSfLrmEh2Aa8KY4bxnuNjcwAr9nXk1zsSgvv70cWjL6UMMSECpSjK2NTUIGz%2BHNZcXAkwHtwA2r8vH8Avypm5AHW%2BCOvDI7oORTkRCr7%2F%2BDmq5947T8FabfRBmHaF301dvM9cdIqHAuqT%2FFh0uV12mo03y%2FImTNCa0faQvlvQljjLZ%2Fe8Z09v7z8oLM%2FjUjBiKLKEhJzxCiPAPd7FG6%2FPtZoueRb0TfEao7ayrIrfSZqTbX8BnFzpQZBm%2BUeXSN4as6p%2F%2B8HliWv%2FRBXCXJQDStyaVHB1%2FnC121eXQbkVDTmRaPYsw2A2RLGxA3SaDx52mzCpj7i6BjrjAoXoOD1e2PKi%2BDKU%2BmJkJ3iC7yr6IYsUzZs61sWkq5VFLjeaDA9NQYwj%2BHsj6C3Vrc2eFdCuSlgZQx5V7nRyTbrv0DzlrYcxHJ7c1I2QeOcLGsBTPIhcCS0bV7FQlWTwp2km9Z5auE%2FAha7GvYdZONPTnfTRZfHpktQOayCxlfGZflNCyBO397Acoil7up5sdLqH1z1aW1aV%2BlVX2eKRLx%2BlOsUvpGnjHfm8Qf3qEet%2F3ODrijZ7VdIh7szQ8KVc6XRmgDAyLagyzW2QRcUbP9LGSOoStRNGGWEVMjjrrjCbh5ytjt3tFfkanRfq5NEQ8A0Tv603VArzU96lJeJq%2FcMU6HgTn0qi3gNrO3E9NjgqhViHCSqN2wvsTStH%2FLPu16rvlopWj5pFEHPFUB72xvcTxUQSCl0t46cXg3vF3kt61u3mchZQ7pyeMUtnnilwY0Gigq0OL5i54l8sAO33E1XTKMA%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ASIAQ4NXQEUIPI37C7EU%2F20241202%2Feu-west-1%2Fs3%2Faws4_request&X-Amz-Date=20241202T193928Z&X-Amz-Expires=7200&X-Amz-SignedHeaders=host&X-Amz-Signature=378e12fb386129fea02e808a94f15998ad81678eb2306f2354fa7915ce38b2fe'
webhook_url = 'https://91a2-2001-1c04-4a0b-b100-30db-5b22-7b7f-6920.ngrok-free.app/pyannote-webhook'
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

