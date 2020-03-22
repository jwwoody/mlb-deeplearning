import os
import json
import string
import random
import subprocess
import multiprocessing
import uuid

def local_clip(filename, start_time, duration, output_filename, output_directory):
    end_time = start_time + duration
    command = ['ffmpeg',
               '-i', '"%s"' % filename,
               '-ss', str(start_time),
               '-t', str(end_time - start_time),
               '-c:v', 'copy', '-an',
               '-threads', '1',
               '-loglevel', 'panic',
               os.path.join(output_directory,output_filename)]
    command = ' '.join(command)

    try:
        output = subprocess.check_output(command, shell=True,
                                         stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as err:
        print(err.output)
        return err.output


def wrapper(clip):
    input_directory = '/'
    output_directory = '/'
    duration = clip['end']-clip['start']
    filename = clip['url'].split('=')[-1]
    print(clip)
    clipName = filename + str(uuid.uuid4())[:8]
    local_clip(os.path.join(input_directory,filename+'.mkv'), clip['start'], duration, clipName+'.mp4', output_directory)
    return 0
    


if __name__ == '__main__':
    with open('data/mlb-youtube-segmented.json', 'r') as f:
    # with open('data/mlb2.json', 'r') as f:
        data = json.load(f)
        pool = multiprocessing.Pool(processes=8)
        pool.map(wrapper, [data[k] for k in data.keys()])
    
