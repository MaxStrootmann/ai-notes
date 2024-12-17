from openai import OpenAI
from email_service import send_email
client = OpenAI()

def get_notes(conversation):
    response = client.chat.completions.create(
        model="gpt-4o-2024-08-06",
        messages=[
            {
                "role": "system", 
                "content": (
                    "Ik ben een bedrijfssoftwareconsultant en jij bent mijn assistent-notulist en coach voor bedrijfs- en verkoopgesprekken. "
                    "Je moet gedetailleerde aantekeningen maken van het telefoongesprek. Geef feedback over mijn communicatie- en verkoopvaardigheden. "
                    "Wanneer relevant, geef een lijst met acties/stappen per spreker. Zorg er ook voor dat je een korte samenvatting van het gesprek geeft."
                )
            },
            {
                "role": "user", 
                "content": f"Gesprek: {conversation}"
            }
        ],
        response_format={
            "type": "json_schema",
            "json_schema": {
                "name": "notes_schema",
                "schema": {
                    "type": "object",
                    "properties": {
                        "title": {
                            "description": "Een duidelijke en beschrijvende titel om dit gesprek later te kunnen identificeren in een lijst met notities.",
                            "type": "string"
                        },
                        "summary": {
                            "description": "Een beknopte samenvatting van het gesprek, maximaal 100 woorden, die de belangrijkste aandachtspunten en conclusies samenvat.",
                            "type": "string"
                        },
                        "key_points": {
                            "description": "Een lijst met de belangrijkste onderwerpen, kwesties of hoogtepunten die tijdens het gesprek zijn besproken.",
                            "type": "array",
                            "items": { "type": "string" }
                        },
                        "decisions_made": {
                            "description": "Een lijst van alle genomen beslissingen, samen met de reden waarom deze beslissingen zijn genomen.",
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "decision": { "type": "string" },
                                    "reason": { "type": "string" }
                                },
                                "required": ["decision", "reason"]
                            }
                        },
                        "todo_list": {
                            "description": "Een lijst met actiepunten die zijn toegewezen aan elke deelnemer in het gesprek, gegroepeerd per spreker.",
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "speaker": { "type": "string" },
                                    "action_items": {
                                        "type": "array",
                                        "items": { "type": "string" }
                                    }
                                },
                                "required": ["speaker", "action_items"]
                            }
                        },
                        "feedback": {
                            "description": "Feedback op mijn communicatie en verkoop vaardigheden als beginnend software consultant",
                            "type": "string"
                        },
                    },
                    "required": ["title", "summary", "key_points", "decisions_made", "todo_list", "feedback"],
                    "additionalProperties": False
                }
            }
        }
    )
    
    print(response.choices[0].message.content)
    send_email(response.choices[0].message.content)
