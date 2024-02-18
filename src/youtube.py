import os
import subprocess
from pytube import YouTube

def download_video(url):
    output_dir = './output'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    yt = YouTube(url)
    
    stream = yt.streams   

    print(str(video))
    
    video.download(output_dir)
    
    return os.path.join(output_dir, video.default_filename)

def convert_to_mp4(input_file_path, output_dir):
    output_file_path = os.path.join(output_dir, 'output.mp4')
    subprocess.run(['ffmpeg', '-i', input_file_path, '-codec', 'copy', output_file_path])
    return output_file_path

if __name__ == "__main__":
    url = input("Enter the YouTube video URL: ")
    try:
        video_file_path = download_video(url)
        output_file_path = convert_to_mp4(video_file_path, './output')
        print(f"Video downloaded and converted successfully: {output_file_path}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
