

import os
with open('extract_frames.sh', 'w') as fout:
    for i in range(0, 500):
        os.makedirs(f'video_frames/{i}',exist_ok = True)
        #fout.write(f'ffmpeg -i video/{i}.mkv -map 0:a -acodec copy audio/{i}.mp3\n')
        fout.write(f'ffmpeg -i video/{i}.mkv -vf fps=fps=1/1 video_frames/{i}/%05d.jpg\n')

