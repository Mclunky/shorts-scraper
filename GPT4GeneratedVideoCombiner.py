import csv, time, os, random
from moviepy.editor import VideoFileClip, CompositeVideoClip


def combine_videos(main_video_path, reaction_video_path, output_path):
    # Load the main video (vertical format)
    main_video = VideoFileClip(main_video_path)
    
    # Load the reaction video (landscape format)
    reaction_video = VideoFileClip(reaction_video_path)

    # Mute the reaction video
    reaction_video = reaction_video.without_audio()

    # Calculate the maximum possible start time for the reaction video
    max_start_time = reaction_video.duration - main_video.duration
    if max_start_time > 0:
        start_time = random.uniform(0, max_start_time)
        reaction_video = reaction_video.subclip(start_time, start_time + main_video.duration)
    else:
        reaction_video = reaction_video.subclip(0, main_video.duration)

    # Resize the reaction video to be smaller, keeping its aspect ratio
    reaction_video = reaction_video.resize(height=main_video.size[1] // 3)

    # Calculate the position for the reaction video
    reaction_x = (main_video.size[0] - reaction_video.size[0]) // 2
    reaction_y = main_video.size[1] - reaction_video.size[1]

    # Overlay the reaction video onto the main video
    final_video = CompositeVideoClip([main_video, reaction_video.set_position((reaction_x, reaction_y))])
    
    # Export the final video
    final_video.write_videofile(output_path, codec='libx264', audio_codec='aac')

if __name__ == "__main__":
    count = 0
    dir_path = '/home/ohio/video'

    for path in os.listdir(dir_path):
        if os.path.isfile(os.path.join(dir_path, path)):
            count += 1
    print("   ", count, " Videos found in the videos folder, ready to upload...")
    


    main_video_path = "/home/ohio/video/America be like:.mp4"
    reaction_video_path = "/home/ohio/video/Amazing Science Toys_Gadgets 2.mp4"
    


    for i in range(count):

        dataset = "/home/ohio/Downloads/YTdownloader/my_file.csv"
        path = "/home/ohio/Videos"
    
        def download_dataset(dataset, path, i, end=0):
            dir_list = os.listdir(path)
            rows = []

        
            with open(dataset, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    rows.append(row)

            if end==0:
                end = len(rows)

            row = rows[i]
            url = row[0]
            filename = row[1]
            return filename
    
        newTitle=download_dataset(dataset, path, i, 10)
        simp_path = 'video/'+newTitle+'.mp4'.format(str(i+1))

        output_path = '/home/ohio/video/'+(newTitle)+'.mp4'
        combine_videos(main_video_path, reaction_video_path, output_path)

