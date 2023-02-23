import os

with open('../video_list/filtered_urls.txt') as fin:
    urls = fin.readlines()


with open('download.sh', 'w')as fout:
    for id, url in enumerate(urls):
        if os.path.isfile(f"video/{id}.mkv"):
            print(f"Skip the {id} th video.")
            continue
        fout.write(f"twitch-dl download {url.strip()} -q 160p -o video/{id}.mkv\n")