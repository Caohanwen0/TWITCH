from correlation_volume import get_volume_result, normalize_list
from get_gift import get_gift
import pandas as pd
import os
# gift - volume correlation

def gift_volume_per_video(video_id, single_video):
    volumes = get_volume_result(video_id)
    gifts = get_gift(f"clean/{video_id}.csv")
    # if there are gift in that second, 
    # plot scatter
    import matplotlib.pyplot as plt
    volume_list, gift_list = [], []
    for item in gifts:
        gift, time_in_second = item
        time_in_second= int(time_in_second)
        if pd.isna(gift) == False:
            gift = float(gift)
            try:
                volume_list.append(volumes[time_in_second])
            except IndexError:
                volume_list.append(0)
            gift_list.append(gift)
    if single_video:
        plt.scatter(volume_list, gift_list, s=1)
        plt.xlabel("Volume")
        plt.ylabel("Gift Sum")
        plt.title(f"Gift Sum vs. Volume of {video_id}")
        plt.show()
    else:
        return volume_list, gift_list


# get ids
ids = os.listdir('video/volume')
ids = [id.split('.')[0] for id in ids]
ids = [id for id in ids if os.path.exists(f"clean/{id}.csv")]
volume_list, gift_list = [], []
for id in ids:
    v, g = gift_volume_per_video(id, False)
    volume_list += v
    gift_list += g
# plot
import matplotlib.pyplot as plt
plt.scatter(volume_list, gift_list, s=1)
plt.xlabel("Volume(multi videos)")
plt.ylabel("Gift Sum")
plt.show()