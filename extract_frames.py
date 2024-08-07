

import os

def generate_frame_every_sec():
    video_number = len(os.listdir('video/video'))
    with open('extract_frames.sh', 'w') as fout:
        for i in range(0, video_number):
            os.makedirs(f'video_frames/{i}',exist_ok = True)
            #fout.write(f'ffmpeg -i video/{i}.mkv -map 0:a -acodec copy audio/{i}.mp3\n')
            fout.write(f'ffmpeg -i video/video/{i}.mkv -vf fps=fps=1/1 video_frames/{i}/%05d.jpg\n')


