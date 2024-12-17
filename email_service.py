import os
import json
from dotenv import load_dotenv
import resend


def send_email(data):
    load_dotenv()
    resend.api_key = os.getenv("RESEND_API_KEY")

    data = json.loads(data)

    html_template = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Business Call Notes</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f4f4f9;
                margin: 0;
                padding: 20px;
                color: #333;
            }}
            .container {{
                background-color: #ffffff;
                max-width: 800px;
                margin: 20px auto;
                border-radius: 10px;
                overflow: hidden;
                box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            }}
            .header {{
                background-color: #007BFF;
                color: white;
                padding: 20px;
                text-align: center;
            }}
            .content {{
                padding: 20px;
            }}
            .section {{
                margin-bottom: 20px;
            }}
            .section-title {{
                font-size: 18px;
                font-weight: bold;
                color: #007BFF;
                margin-bottom: 10px;
                border-bottom: 2px solid #007BFF;
                padding-bottom: 5px;
            }}
            .list-item {{
                margin-left: 20px;
            }}
            .list-item ul {{
                padding-left: 20px;
            }}
            .list-item li {{
                margin-bottom: 8px;
            }}
            .footer {{
                text-align: center;
                padding: 20px;
                background-color: #007BFF;
                color: white;
                font-size: 14px;
            }}
            .footer a {{
                color: #ffffff;
                text-decoration: none;
            }}
        </style>
    </head>
    <body>
    
    <div class="container">
        <div class="header">
            <h1>Business Call Notes</h1>
        </div>
    
        <div class="content">
            
            <!-- Title Section -->
            <div class="section">
                <div class="section-title">Title</div>
                <p>{data['title']}</p>
            </div>
            
            <!-- Summary Section -->
            <div class="section">
                <div class="section-title">Summary</div>
                <p>{data['summary']}</p>
            </div>
    
            <!-- Key Points Section -->
            <div class="section">
                <div class="section-title">Key Points</div>
                <ul class="list-item">
                    {''.join(f'<li>{point}</li>' for point in data['key_points'])}
                </ul>
            </div>
    
            <!-- Decisions Made Section -->
            <div class="section">
                <div class="section-title">Decisions Made</div>
                <ul class="list-item">
                    {''.join(f'<li><strong>Decision:</strong> {decision["decision"]} <br><strong>Reason:</strong> {decision["reason"]}</li>' for decision in data['decisions_made'])}
                </ul>
            </div>
    
            <!-- To-Do List Section -->
            <div class="section">
                <div class="section-title">To-Do List</div>
                {''.join(f'''
                <div class="list-item">
                    <strong>Speaker: {todo['speaker']}</strong>
                    <ul>
                        {''.join(f'<li>{action}</li>' for action in todo['action_items'])}
                    </ul>
                </div>''' for todo in data['todo_list'])}
            </div>
    
        </div>
    
        <div class="footer">
            <p>AI-notes by Max Strootmann</p>
            <p><a href="https://example.com">View More Details</a></p>
        </div>
    </div>
    
    </body>
    </html>
    """


    params: resend.Emails.SendParams = {
        "from": "AI-notes <max@nngrafischontwerp.nl>",
        "to": ["max@kennismetai.nl"],
        "subject": f"{data["title"]}",
        "html": html_template,
    }
    
    resend.Emails.send(params)

