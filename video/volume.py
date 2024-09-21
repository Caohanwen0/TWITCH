import os
import subprocess
from pydub import AudioSegment
import numpy as np

VIDEO_FOLDER = "../GTA_video"
SAVE_FOLDER = "../GTA_video_volume"
os.makedirs(SAVE_FOLDER, exist_ok=True)

def is_file_empty(file_path):
    return os.path.getsize(file_path) == 0

def check_log_status(file_id):
    # Check if file exists
    if os.path.exists(f'../clean/{file_id}.csv') and not is_file_empty(f'../clean/{file_id}.csv'):
        print(f"File {file_id}.csv already exists. Start processing volume of the corresponding file.")
        return True
    else:
        return False

def get_max_volume(videoname, output_file, file_id):
    if check_log_status(file_id):
        if os.path.exists(output_file) and not is_file_empty(output_file):
            print(f"File {file_id}.txt already finished parsing.")
            return
        max_volumes(videoname)
    else:
        print(f"File {file_id}.csv does not exist.")
        return

def save_volumes(volumes, output_file):
    with open(output_file, 'w') as f:
        for volume in volumes:
            f.write(f"{volume}\n")

def max_volumes(videoname):

    def convert_to_wav(input_file):
        output_file = os.path.splitext(input_file)[0] + ".wav"
        subprocess.run(["ffmpeg", "-i", input_file, "-acodec", "pcm_s16le", "-ar", "44100", output_file], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return output_file

    def get_max_volume_each_second(filename):
        audio = AudioSegment.from_wav(filename)

        duration_seconds = int(audio.duration_seconds)
        max_volumes = []

        for second in range(duration_seconds):
            start_time = second * 1000  # Convert seconds to milliseconds
            end_time = start_time + 1000

            segment = audio[start_time:end_time]
            samples = np.array(segment.get_array_of_samples())
            max_volume = np.max(np.abs(samples)) / 32768.0  # Normalize to the range [-1, 1]

            max_volumes.append(max_volume)

        return max_volumes

    filename = f'{VIDEO_FOLDER}/{videoname}'
    wav_filename = convert_to_wav(filename)  # Convert any input format to WAV
    max_volumes = get_max_volume_each_second(wav_filename)
    save_volumes(max_volumes[1:], f'{SAVE_FOLDER}/{os.path.splitext(videoname)[0]}.txt')
    # Remove the temporary WAV file if needed
    os.remove(wav_filename)  # Optional: Remove WAV file after processing

# Get the list of files in the video folder
video_list = os.listdir(VIDEO_FOLDER)

# Filter files that end with ".mkv" or ".m4a"
video_list = [video for video in video_list if video.endswith('.mkv') or video.endswith('.m4a')]

for video in video_list:
    print(f"Processing video {video}...")
    max_volumes(video)
