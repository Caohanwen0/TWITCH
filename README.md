# HOW TO PREPARE A TWITCH DATASET

## url & metadata

首先按照[官方指南](https://dev.twitch.tv/docs/api/get-started/)在twitch申请app access token

然后按照以下流程进行指令：

（如果肉身在gfw内，开全局vpn似乎也不能正常运行，我当时是拜托美国的朋友帮我跑的）

```terminal
# obtain oAuth token
curl -X POST 'https://id.twitch.tv/oauth2/token' \
-H 'Content-Type: application/x-www-form-urlencoded' \
-d 'client_id=bj2t17usp0k0mgh54ejax7fduw8mpm&client_secret=82uv9v52s7j0toiz2w7em0x8byls1v&grant_type=client_credentials'

# 获取用户信息（这一步在接下来需要用到）
curl -X GET 'https://api.twitch.tv/helix/users?login=twitchdev' \
-H 'Authorization: Bearer fwviomszf7navy8x6jikkf2q5gve94' \
-H 'Client-Id: bj2t17usp0k0mgh54ejax7fduw8mpm'

# 查询game id
# 用游戏名称查询game id，这里使用的是minecraft
curl -H 'Client-ID: bj2t17usp0k0mgh54ejax7fduw8mpm' \
-H 'Authorization: Bearer fwviomszf7navy8x6jikkf2q5gve94' \
-X GET 'https://api.twitch.tv/helix/games?name=Minecraft'
# 运行结果：
# {"data":[{"id":"27471","name":"Minecraft","box_art_url":"https://static-cdn.jtvnw.net/ttv-boxart/27471_IGDB-{width}x{height}.jpg","igdb_id":"121"}]}

# Getting video by game
# 对于不同的游戏，需要更改game_id
# first：这里的first参数是需要返回多少个视频（最大就是100，所以如果需要多于100个视频，需要反复运行这个指令）
# after：在每一次运行之后，会返回一个after参数，用于翻页获取下一页的视频。每次重新运行这个指令的时候需要修改after（第一次after不需要指定
# language：这里是主播的language，这里指定为英语（en）
curl -X GET 'https://api.twitch.tv/helix/videos?game_id=27471&language=en&sort=views&first=100&after=eyJiIjp7Ik9mZnNldCI6Mjk3fSwiYSI6eyJPZmZzZXQiOjQ5NX19' \
-H 'Authorization: Bearer bm3x6tex3np3gttk0j7zrnoz1ol8ie' \
-H 'Client-Id: bj2t17usp0k0mgh54ejax7fduw8mpm' 
# 这里返回的是json格式，这里得到的除了url，还有视频的一些metadata，可以直接重定向到文件里保存下来。
```

## video download

### 脚本生成

直接运行`video/download.py`（生成的是使用twitch-dl的脚本，如果不能正常运行的话可以修改43行的注释改用Downloader）

### 工具（二选一）

twitch-dl:

```
pip install twitch-dl
```

TwitchDownloader:

https://github.com/lay295/TwitchDownloader 

(我直接下载了executable。需要把文件放在video/文件夹下）

### 帧抽取

* install ffmpeg；

* 运行`extract_frame.py`生成脚本（每一秒进行一次截图；每个视频的结果保存在对应编号的文件夹下）

## audio transcription

* install whisper:

  ```
  pip install whisper
  ```

* 运行`video/transcribe.py`

## audio volume

* install ffprobe
* 运行`video/volume.py`，结果会保存在`./video/volume`文件夹下
* 格式：每一行为一个数字，对应的是视频每一秒主播的最大音量

## chat log scrapping

### scrapping

安装chat_downloader

```
pip install chat_downloader
```

运行`scrap_chat_log.sh`中的write_executive函数，得到脚本`scrap_chat_log.sh`。结果会保存在`./chat_log`文件夹下

然后运行write_to_csv函数，将json文件处理为csv格式。处理后的csv文件保存在`./clean`文件夹下
