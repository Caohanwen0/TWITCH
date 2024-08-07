import os,csv
from urllib.parse import urlparse

def is_valid_url(url):
    """
    Check if a string is a valid URL
    """
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False

def get_url_list():
    l = os.listdir('../clean')
    urls = []
    for csvname in l:
        with open(os.path.join('../clean', csvname)) as fin:
            try:
                csvreader = csv.reader(fin)
                for step, row in enumerate(csvreader):
                    if step == 0:
                        continue
                    else:
                        if is_valid_url(row[7]):
                            urls.append(row[7])
                        break
            except UnicodeDecodeError:
                print(csvname)
    return urls


# with open("clean_url", "w")as fout:
#     for url in urls:
#         fout.write(url + "\n")


