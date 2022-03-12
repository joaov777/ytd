# REQUIRED LIBRARIES
from fileinput import filename
from pytube import YouTube
import os
import time as t
from pytube.cli import on_progress
import re
import imageio_ffmpeg
import subprocess as sp

ffmpeg_url = imageio_ffmpeg.get_ffmpeg_exe()
standard_header="### -- YOUTUBE VIDEO DOWNLOADER -- ###"

#defining colors
CBLUE = "\33[34m"
CEND = "\33[0m"
CRED = "\33[31m"

#for headers and better UI
def header(header, screen_clear="False"):
    
    if screen_clear == True: clear_screen()
    print(f"{header}")
  
# clearing the screen 
def clear_screen():
    os.system("cls") if os.name == "nt" else os.system("clear")

# remove unused files
def cleaner(file_name):
    if os.path.exists(file_name) : 
        os.remove(file_name)
        return True
    else: 
        return False

# checking video timestamps both for pattern and inconsistency
def check_timestamps(video_url, start_time, end_time):
    """- Check whether timestamps make sense for the pattern HH:MM:SS"""

    yt = YouTube(video_url, on_progress_callback=on_progress)

    #regex to validate HH:MM:SS format
    match_timestamp = re.compile(r'^[0-9][0-9]{1}\:[0-9][0-9]\:[0-9][0-9]$' , re.IGNORECASE)

    #verifying whether start_time and end_time follow the format
    if re.match(match_timestamp, start_time) and re.match(match_timestamp, end_time):
        if time_to_sec(start_time) < time_to_sec(end_time) and time_to_sec(start_time) >= time_to_sec("00:00:00") and time_to_sec(end_time) <= yt.length:
            print(CBLUE + "> Timestamps valid!" + CEND)
            t.sleep(1)
            return True
        else:
            print(CRED + "> Timestamps invalid!" + CEND)
            input("> Press any key to continue...")
            return False
    else:
        print(CRED + "> Timestamps misformatted! Insert HH:MM:SS (Hours, Minutes, Seconds)" + CEND)
        input("> Press any key to continue...")
        return False

# checking whether a Youtube URL is valid
def check_url(url):
    """Validate Youtube URL parameter locally and remotely"""

    #checks if the youtube url is semmantically correct
    #accepts all options below: 
    #-- www.youtube.com/watch?v=ADNlX5O_j0E
    #-- www.youtube.com/watch?v=ADNlX5O_j0E
    #-- https://www.youtube.com/watch?v=ADNlX5O_j0E
    #-- https://youtube.com/watch?v=ADNlX5O_j0E
    #-- http://www.youtube.com/watch?v=ADNlX5O_j0E
    #-- http://youtube.com/watch?v=ADNlX5O_j0E
    #-- https://youtu.be/ADNlX5O_j0E
    #-- http://youtu.be/ADNlX5O_j0E
    #-- youtube.com/watch?v=ADNlX5O_j0E
    #-- youtu.be/ADNlX5O_j0E
    match_url = re.compile(r'^(https?\:\/\/)?((www\.)?youtube\.com|youtu\.be)\/(watch\?v=)?.+$', re.IGNORECASE)

    if re.match(match_url, url) is not None:
        try: 
            yt = YouTube(url)
            return True
        except:
            return False
    else:
        return False
    
# downloading the video from youtube
def download_video(yt,final_video_name):

    header(standard_header, True)
    print(CBLUE + f"> Downloading: {yt.title}" + CEND)

    video = yt.streams.get_highest_resolution()
    video.download(filename=f"{final_video_name}.mp4")
   
# cutting the video by section
def cut_video(video_local_url, start_time, end_time, final_file):

    print("- Cutting your video...")
    sp.call([ffmpeg_url, '-loglevel', 'quiet', '-ss', start_time, '-to', end_time, '-i', video_local_url, '-c', 'copy', f"{final_file}.mp4"])

def cut_audio(yt,input_file, start_time, end_time, final_name):

    download_video(yt,final_name) 
    sp.call([ffmpeg_url, '-loglevel', 'quiet', '-ss', start_time, '-to', end_time, '-i', f"./{final_name}.mp4", '-q:a', '0', '-map', 'a', f"{final_name}_YTD-audio.mp3"])
    cleaner(f"./{final_name}.mp4")

def extract_audio(yt, final_name):

    download_video(yt,final_name) 
    sp.call([ffmpeg_url, '-loglevel', 'quiet', '-i', f"./{final_name}.mp4", '-q:a', '0', '-map','a', f"{final_name}_YTD-audio.mp3"])
    cleaner(f"./{final_name}.mp4")
    
# downloading and cutting 
def download_and_cut_video(yt,video_url, video_name_after_cut, start_time, end_time):
    
    download_video(yt,"temp_video")
    cut_video(f"./temp_video.mp4", start_time, end_time, video_name_after_cut)

    cleaner("./temp_video.mp4")

    print(f"> Location: {os.getcwd()}")
    input()
 
#converting time to seconds
def time_to_sec(t):
   h, m, s = map(int, t.split(':'))
   return h * 3600 + m * 60 + s
