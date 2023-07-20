import subprocess
import csv
import time
import random
import os
#
#Processing video 21
#2023-07-21 01:49:37 https://www.youtube.com/shorts/b9YtBurBsVM the way the baby dropped the tablet was so smooth and felt so real. she's a natural actor
#/bin/sh: 1: Syntax error: "(" unexpected
#
#can fix this????????????????????????????
def download_video(url, filename):
    # windows command
    #command = f".\\yt-dlp.exe -f bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best -o video/{filename}.%(ext)s {url}"
    # linux command
    command = f"yt-dlp -f bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best -o 'video/{filename}.%(ext)s' '{url}'"
    subprocess.call(command, shell=True)

def download_dataset(dataset, path, sleep=5, start=0, end=0):
    dir_list = os.listdir(path)
    rows = []
    missed_files = []

    with open(dataset, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            rows.append(row)

    if end==0:
        end = len(rows)

    for i in range(start, end):
        print(50*"*")
        print("Processing video", i)
        row = rows[i]
        url = row[0]
        filename = row[1]
        if filename + ".mp4" not in dir_list:
            current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            print(current_time, url, filename)
            download_video(url, filename)
            time.sleep(sleep*random.random())
        else:
            missed_files.append((url, filename))
    print("Missed files:", len(missed_files), "out of", len(rows))
    return filename
dataset = "/home/ohio/Downloads/YTdownloader/my_file.csv"
path = "/home/ohio/Videos"
download_dataset(dataset, path, 5, 0, 300)