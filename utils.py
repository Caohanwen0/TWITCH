'''
utils function 
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
import csv


def get_video_number():
    return len(os.listdir('video/video'))

def get_gift(csv_file_path):
    df = pd.read_csv(csv_file_path, encoding='utf-8')
    # get length of df['view_count']
    # get column x and y
    gift_sum = df['gift_sum']
    time_in_seconds = df['time_in_seconds']
    gift_cnt = 0
    gift_status = []
    for index, gift in enumerate(gift_sum):
        # check if gift is nan in csv
        if pd.isna(gift) == False: 
            gift_cnt += 1
            time_in_second = time_in_seconds[index]
            gift_status.append((gift,time_in_second))

    print(f"Total gift of {csv_file_path} is {gift_cnt}")
    return gift_status
            
            
def get_description(video_id):
    with open(f'clean/{video_id}.csv', 'r') as file:
        # read in csv
        import csv
        reader = csv.DictReader(file)
        # get sentiment
        description = []
        for step, row in enumerate(reader, start = 1):
            # if is not nan
            return row['description']
        
# videolist = os.listdir('clean')
# # filter out those end with ".csv"
# videolist = [video for video in videolist if video.endswith('.csv')]
# video_ids = [video.split('.')[0] for video in videolist]
# cnt, total = 0, len(video_ids)
# for video_id in video_ids:
#     print(f"[info] Processing video : {video_id}...")
#     description = get_description(video_id)
#     if len(description) > 0:
#         print(f"[info] Description : {description}")
#         cnt += 1

# print(f"[info] {cnt} out of {total} videos have description.")

    
def fit_linear(x, y, xlabel, ylabel, title = None, grid = True):
    import matplotlib.pyplot as plt
    import numpy as np
    from scipy import stats
    slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
    x = np.array(x)

    linear_fit = slope * x + intercept

    print(f"Correlation coefficient (r): {r_value}")
    print(f"P-value: {p_value}")
    print(f"Standard error: {std_err}")

    plt.scatter(x, y, label='Scatter Plot')
    plt.plot(x, linear_fit, color='red', label='Linear Fit')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    if title is None:
        title = f"{ylabel} 2 {xlabel}"
    plt.title(title)
    plt.legend()
    plt.grid(grid