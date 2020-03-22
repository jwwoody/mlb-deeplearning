import os
import json
import string
import random
import subprocess


save_dir = '/data'
with open('data/mlb-youtube-segmented.json', 'r') as f:
    data = json.load(f)
    count = 0
    for entry in data:
        yturl = data[entry]['url']
        ytid = yturl.split('=')[-1]

        if os.path.exists(os.path.join(save_dir, ytid+'.mkv')):
            continue
        cmd = 'youtube-dl -f 37/22/18/best '+yturl+' -o '+os.path.join(ytid+'.mkv')
        os.system(cmd)
        count+=1
        if count > 0:
            break
