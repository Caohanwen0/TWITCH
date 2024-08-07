import os
from utils import get_video_number
with open('audio.sh', 'w') as fout:
    video_number = get_video_number()
    for i in range(0, video_number):
        fout.write(f'ffmpeg -i video/{i}.mkv -map 0:a -acodec libmp3lame audio/{i}.mp3\n')

