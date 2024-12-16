from openai import OpenAI
client = OpenAI()

def main():

  with open("./2dekamer.mp3", "rb") as recording:
    transcription = client.audio.transcriptions.create(
      model="whisper-1", 
      file=recording
    )
    print(transcription.text)

main()

    # Code should run when a new recording is added to the folder
    
    # Find and open new recording
    
    # Send to whisper and store transcription in db
    
    # Get the transcription and original audio file and email them
    
    # Send the transcription to chatGPT to have it summarized
    
    # Store the summary in the db and email it
    
    # Send it to chatgpt to have it give sales advice
    
    # Store the advise in the db and email it
    
    
    
    
