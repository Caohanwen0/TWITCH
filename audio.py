

import os
with open('audio.sh', 'w') as fout:
    for i in range(0, 500):
        fout.write(f'ffmpeg -i video/{i}.mkv -map 0:a -acodec libmp3lame audio/{i}.mp3\n')

