import os
import resend

def send_email(data):
    if not data:
        data = "Hello world"

    resend.api_key = os.getenv("RESEND_API_KEY")
    params: resend.Emails.SendParams = {
        "from": "AI-notes <max@nngrafischontwerp.nl>",
        "to": ["max@kennismetai.nl"],
        "subject": "hello world",
        "html": f"<p>{data}</p>",
    }
    
    email = resend.Emails.send(params)


if __name__ == "__main__":
    send_email()
