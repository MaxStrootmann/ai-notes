from openai import OpenAI
import json
import ffmpeg
from take_notes import get_notes

def main():

    text_output_file = f"./transcriptions/conversation.md"

    with open("./test.json", "r") as f:
        file = f.read()
        dict_from_file = json.loads(file)
        diarization = dict_from_file["output"]["diarization"]
        print(diarization)

        # use ffmpeg to make chunk recording per speaker
        for i in range(4):
            speaker = diarization[i + 1]["speaker"]
            start_time = diarization[i + 1]["start"]
            end_time = diarization[i + 1]["end"]
            chunk_duration = float(end_time) - float(start_time)
            # print(f"start: {start_time}, chunk: {chunk_duration}")

            file_path = "./2dekamer.mp3"
            output_path = f"./chunks/{speaker}_chunk{i}.mp3"

            (
                ffmpeg
                    .input(file_path, ss=start_time, t=chunk_duration)  # Start at i, take chunk_duration seconds
                    .output(output_path, codec='copy')  # Copy the audio without re-encoding
                    .run(overwrite_output=True)       
            )
             # Transcribe the chunk
            client = OpenAI()
            
            audio_file= open(file_path, "rb")
            transcription = client.audio.transcriptions.create(
            model="whisper-1", 
            file=audio_file
            )
            print(transcription.text)

            with open(text_output_file, 'a') as f:
                diarized_transcription = f"{speaker}: " + transcription.text + "\n\n"
                f.write(diarized_transcription)

    with open(text_output_file, 'r') as f:
        conversation = f.read()
        get_notes(conversation)


            
            

if __name__ == "__main__":
    main()
