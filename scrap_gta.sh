# chat_downloader https://www.twitch.tv/videos/2239261334 --output GTA_chat_log/0.json
# chat_downloader https://www.twitch.tv/videos/2240203652 --output GTA_chat_log/1.json
# chat_downloader https://www.twitch.tv/videos/2241848432 --output GTA_chat_log/2.json
# chat_downloader https://www.twitch.tv/videos/2241075087 --output GTA_chat_log/3.json
# chat_downloader https://www.twitch.tv/videos/2242714837 --output GTA_chat_log/4.json

twitch-dl download https://www.twitch.tv/videos/2239261334 -q 160p -o GTA_video/0.mkv
ffmpeg -i "GTA_video/0.mkv" -vn -acodec aac -b:a 128k -ar 22050 -ac 1 "GTA_video/0.m4a"
cd video
python volume.py
python transcribe.py

twitch-dl download https://www.twitch.tv/videos/2241075087 -q 160p -o GTA_video/3.mkv
ffmpeg -i GTA_video/3.mkv -vf fps=fps=1/1 GTA_video_frames/3/%05d.jpg
ffmpeg -i "GTA_video/3.mkv" -vn -acodec aac -b:a 128k -ar 22050 -ac 1 "GTA_video/3.m4a"
cd video
python volume.py
python transcribe.py
cd ..
rm GTA_video/3.mkv
rm GTA_video/3.m4a

twitch-dl download https://www.twitch.tv/videos/2242714837 -q 160p -o GTA_video/4.mkv
ffmpeg -i GTA_video/4.mkv -vf fps=fps=1/1 GTA_video_frames/4/%05d.jpg
ffmpeg -i "GTA_video/4.mkv" -vn -acodec aac -b:a 128k -ar 22050 -ac 1 "GTA_video/4.m4a"
cd video
python volume.py
python transcribe.py
cd ..
rm GTA_video/4.mkv
rm GTA_video/4.m4a

