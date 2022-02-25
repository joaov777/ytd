# REQUIRED LIBRARIES
from asyncio.log import logger
from importlib.resources import path
from tkinter.ttk import Progressbar
from tracemalloc import start
from pytube import YouTube
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.editor import *
from os import system, name
import os
import time as t
from pytube.cli import on_progress
import pytube.cli as ptc
import re

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
        print("> Timestamps valid!")
        t.sleep(1)
        return True
    else:
        print("> Start time is lower/equal to End Time!")
        t.sleep(1)
        return False

# checking whether a Youtube URL is valid
def check_url(video_url_or_file_name):
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

    if re.match(match_url, video_url_or_file_name) is not None:
        try: 
            yt = YouTube(video_url_or_file_name)
            print(f"> Valid Youtube URL!")
            t.sleep(1)
            return True
        except:
            print("> Invalid Youtube video!")
            t.sleep(1)
            return False

    else:
        print("> Invalid Youtube URL!")
        t.sleep(1)
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
    #ffmpeg_extract_subclip(r"{}".format(video_local_path), time_to_sec(start_time), time_to_sec(end_time), targetname=f"{final_file}.mp4")
    clip = VideoFileClip(video_local_path).subclip(start_time,end_time)
    final = concatenate_videoclips([clip]).write_videofile(f"./{final_file}.mp4", verbose=False, logger=None)

# downloading and cutting 
def download_and_cut_video(video_url, video_name_after_cut, start_time, end_time):
    
    download_video(video_url,"temp_video")
    cut_video(f"./temp_video.mp4", start_time, end_time, video_name_after_cut)

    #os.remove("./temp_video.mp4") if os.path.exists("./temp_video.mp4") else print("- File not found! ")

    print(f"> Location: {os.getcwd()}")
    input()
 
#converting time to seconds
def time_to_sec(t):
   h, m, s = map(int, t.split(':'))
   return h * 3600 + m * 60 + s