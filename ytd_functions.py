# REQUIRED LIBRARIES
from pytube import YouTube, Playlist, Channel
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from os import system, name
import os
import time as t
from tqdm import tqdm, trange
import threading
from pytube.cli import on_progress
import pytube.cli as ptc

standard_header=">> YOUTUBE VIDEO DOWNLOADER <<"

#for headers and better UI
def header(header, screen_clear="False"):
    
    if screen_clear == True: clear_screen()
    print(f"{header}")

# clearing the screen 
def clear_screen():
    system("cls") if name == "nt" else os.system("clear")

# checking video timestamps both for pattern and inconsistency
def check_timestamps(start_time, end_time):
    """- Check whether timestamps make sense for the pattern HH:MM:SS"""
    #return True if time_to_sec(start_time) <= time_to_sec(end_time) else False
    if time_to_sec(start_time) < time_to_sec(end_time):
        return True
    else:
        print("> Start time is lower/equal to End Time!")
        input()
        return False

# checking whether a Youtube URL is valid
def check_url(video_url):
    """Check Youtube url parameter"""
    return True
    
# downloading the video from youtube
def download_video(video_url, final_video_name):
    
    yt = YouTube(video_url, on_progress_callback=on_progress)

    header(standard_header, True)
    print(f"> Downloading: {yt.title}")

    # if no output name is provided by the user
    #if final_video_name == "": final_video_name = str(yt.title)[0]

    video = yt.streams.get_highest_resolution()
    video.download(filename=f"{final_video_name}.mp4")
    
# cutting the video by section
def cut_video(video_local_path, start_time, end_time, final_file):

    print("- Cutting your video...")
    ffmpeg_extract_subclip(r"{}".format(video_local_path), time_to_sec(start_time), time_to_sec(end_time), targetname=f"{final_file}.mp4")

# downloading and cutting 
def download_and_cut_video(video_url, video_name_after_cut, start_time, end_time):
    
    download_video(video_url,"temp_video")
    cut_video(r"./temp_video.mp4", start_time, end_time, video_name_after_cut)

    os.remove("./temp_video.mp4") if os.path.exists("./temp_video.mp4") else print("- File not found! ")
 
#converting time to seconds
def time_to_sec(t):
   h, m, s = map(int, t.split(':'))
   return h * 3600 + m * 60 + s