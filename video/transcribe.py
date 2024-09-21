import whisper
import csv
import os
from pydub import AudioSegment

def split_audio(audio_file_path, num_pieces=10):
    """
    Splits the audio file into approximately 'num_pieces' smaller chunks.
    Returns a list of file paths to the smaller chunks.
    """
    # Load the audio file (automatically detects format)
    audio = AudioSegment.from_file(audio_file_path)
    duration_ms = len(audio)  # Duration of the audio in milliseconds
    chunk_duration = duration_ms // num_pieces  # Duration of each chunk
    
    audio_chunks = []
    file_format = os.path.splitext(audio_file_path)[1]  # Get file extension
    for i in range(num_pieces):
        start_time = i * chunk_duration
        end_time = (i + 1) * chunk_duration if (i + 1) < num_pieces else duration_ms
        chunk = audio[start_time:end_time]
        chunk_path = f"{audio_file_path.replace(file_format, '')}_chunk{i+1}.wav"
        chunk.export(chunk_path, format="wav")  # Export to WAV for compatibility with Whisper
        audio_chunks.append((chunk_path, start_time / 1000))  # Save chunk path and start time in seconds
    
    return audio_chunks

def transcribe_and_save_csv(audio_file_path, save_folder, num_pieces=10):
    # Ensure the save folder exists
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)

    # Split the audio into smaller chunks
    print(f"Splitting {audio_file_path} into {num_pieces} pieces...")
    audio_chunks = split_audio(audio_file_path, num_pieces)

    # Load Whisper model
    model = whisper.load_model("base")

    # Prepare CSV file path
    file_name = os.path.basename(audio_file_path).replace('.wav', '').replace('.m4a', '') + '_transcription.csv'
    csv_file_path = os.path.join(save_folder, file_name)

    # Open the CSV file to write transcription with timestamps
    with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["start time (s)", "end time (s)", "text"])

        # Loop through each chunk, transcribe it, and adjust the timestamps
        for chunk_path, chunk_start_time in audio_chunks:
            print(f"Transcribing {chunk_path}...")
            result = model.transcribe(chunk_path)

            # Write each segment's transcription with adjusted timestamps to the CSV
            for segment in result['segments']:
                start_time = segment['start'] + chunk_start_time
                end_time = segment['end'] + chunk_start_time
                text = segment['text']
                writer.writerow([start_time, end_time, text])
    
    print(f"Transcription saved to: {csv_file_path}")

# Example usage:
# Path to the audio file (WAV or M4A)
video_folder = "../GTA_video"
audio_files = os.listdir(video_folder)
audio_files = [f for f in audio_files if (f.endswith('.wav') or f.endswith('.m4a'))]

for audio_file in audio_files:
    audio_file_path = os.path.join(video_folder, audio_file)
    print("Transcribing", audio_file_path)
    transcribe_and_save_csv(audio_file_path, video_folder)
    print("Transcription complete.")
