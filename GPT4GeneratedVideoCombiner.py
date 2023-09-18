import csv, os, random
from moviepy.editor import VideoFileClip, CompositeVideoClip

def prepare_main_video(main_video_path):
    main_video = VideoFileClip(main_video_path)
    return main_video

def prepare_reaction_video(main_video, reaction_video_path):
    reaction_video = VideoFileClip(reaction_video_path).without_audio()

    # Calculate the maximum possible start time for the reaction video
    max_start_time = reaction_video.duration - main_video.duration
    if max_start_time > 0:
        start_time = random.uniform(0, max_start_time)
        reaction_video = reaction_video.subclip(start_time, start_time + main_video.duration)
    else:
        reaction_video = reaction_video.subclip(0, main_video.duration)

    # Resize and position the reaction video
    reaction_video = reaction_video.resize(height=main_video.size[1] // 3)
    reaction_x = (main_video.size[0] - reaction_video.size[0]) // 2
    reaction_y = main_video.size[1] - reaction_video.size[1]
    
    return reaction_video.set_position((reaction_x, reaction_y))

def combine_videos(main_video_path, reaction_video_path, output_path):
    main_video = prepare_main_video(main_video_path)
    reaction_video = prepare_reaction_video(main_video, reaction_video_path)

    # Combine main and reaction videos
    final_video = CompositeVideoClip([main_video, reaction_video])

    # Export the combined video
    final_video.write_videofile(output_path, codec='libx264', audio_codec='aac')

def download_dataset(dataset, path, i, end=0):
    dir_list = os.listdir(path)
    rows = []
    
    with open(dataset, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            rows.append(row)

        if end == 0:
            end = len(rows)

        row = rows[i]
        filename = row[1]
        return filename

if __name__ == "__main__":
    dir_path = '/home/ohio/video'
    video_files = [path for path in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, path))]
    
    print("   ", len(video_files), " Videos found in the videos folder, ready to upload...")

    for video_file in video_files:
        dataset = "/home/ohio/Downloads/YTdownloader/my_file.csv"
        path = "/home/ohio/Videos"
        newTitle = download_dataset(dataset, path, video_files.index(video_file))

        video_path = os.path.join(dir_path, newTitle + '.mp4')
        reaction_video_path = "/home/ohio/video/Amazing Science Toys_Gadgets 2.mp4"

        if os.path.exists(video_path):
            combine_videos(video_path, reaction_video_path, video_path)
