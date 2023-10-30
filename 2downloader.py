import subprocess
import csv
import time
import random
import os

def download_video(url, filename):
    # Forming the command as a list of arguments
    command = [
        'yt-dlp',
        '-f', 'bestvideo+bestaudio',
        '-o', f'Videos/Main/{filename}.%(ext)s',
        '--merge-output-format', 'mp4',
        url
    ]
    # Calling the subprocess without shell=True
    subprocess.call(command)

def download_dataset(dataset, path, sleep=5, start=0, end=0):
    dir_list = os.listdir(path)
    rows = []
    missed_files = []

    # Specifying utf-8 encoding while opening the file
    with open(dataset, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            rows.append(row)

    if end == 0:
        end = len(rows)

    for i in range(start, end):
        print(50 * "*")
        print("Processing video", i)
        row = rows[i]
        url = row[0]
        filename = row[1]
        if filename + ".mp4" not in dir_list:
            current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            print(current_time, url, filename)
            download_video(url, filename)
            time.sleep(sleep * random.random())
        else:
            missed_files.append((url, filename))
    print("Missed files:", len(missed_files), "out of", len(rows))
    return filename


# Dataset file
dataset = "my_file.csv"

# Path to the directory
path = "C:/Users/Ohio/Documents/Shorts Scraper/Videos/Main"

# Calling the download_dataset function
download_dataset(dataset, path, 5, 0, 7)
