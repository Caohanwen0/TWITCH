import whisper, os, csv
video_path = "GTA_video"

model = whisper.load_model("base", device = "mps")
fieldnames = ["audio_text", 
"audio_start_time", 
"audio_end_time", 
"no_speech_prob",
"temperature",
'avg_logprob',
'compression_ratio',
]
# load audio and pad/trim it to fit 30 seconds
def write_to_csv(video):
    audio_save_dir = f"{video_path}_transcription"
    audio_save_path = f"{audio_save_dir}/{video.split('.')[0]}.csv"
    os.makedirs(audio_save_dir, exist_ok=True)
    try:
        video_id = int(video.split("/")[-1].split(".")[0])
    except ValueError:
        print(f"Error parsing {video}...")
        return
    if os.path.isfile(audio_save_path):
        print(f"Skip video {video}...")
        return
    with open(audio_save_path, mode='w') as file:
        writer = csv.DictWriter(file, fieldnames = fieldnames)   
        writer.writeheader()  
        result = model.transcribe(f"{video_path}/{video}",without_timestamps = False)
        segments = result["segments"]
        for sent in segments:
            row = {}
            row["audio_text"] = sent["text"]
            row["audio_start_time"] = sent["start"]
            row["audio_end_time"] = sent["end"]
            row["temperature"] = sent["temperature"]
            row["compression_ratio"] = sent["compression_ratio"]
            row["avg_logprob"] = sent["avg_logprob"]
            row["no_speech_prob"] = sent["no_speech_prob"]
            writer.writerow(row)
    print(f"Finish processing video {video}...")
    
video_list = os.listdir(video_path)
for filename in video_list:
    write_to_csv(filename)