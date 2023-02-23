import whisper, os

model = whisper.load_model("base")
fieldnames = ["audio_text", "audio_start_time", "audio_end_time", "no_speech_prob"]
# load audio and pad/trim it to fit 30 seconds
def write_to_csv(video):
    video_id = int(video.split(".")[0])
    with open(f"transcription/{video_id}.csv", "w") as file:
        writer = csv.DictWriter(file, fieldnames = fieldnames)   
        writer.writeheader() 
        result = model.transcribe(video, without_timestamps = False)
        segments = result["segments"]
        for sent in segments:
            row = {}
            row[]

    
