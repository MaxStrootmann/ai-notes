import resend
import os
from dotenv import load_dotenv


def get_data():

    load_dotenv()
    resend.api_key = os.getenv("RESEND_API_KEY")

    params: resend.Emails.SendParams = {
        "from": "Acme <onboarding@resend.dev>",
        "to": ["delivered@resend.dev"],
        "subject": "hello world",
        "html": "<strong>it works!</strong>",
    }
    
    email = resend.Emails.send(params)
