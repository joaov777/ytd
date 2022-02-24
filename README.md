# ytd-cli

**Python script for downloading <u>[Youtube®](https://youtube.com)</u> videos at the highest video and audio quality.** 

## Features

- Download Youtube videos (Full length or sections)
- Download Youtube audio track (Full length or sections)
- Extract video and/or audio from local video files (Full length or sections)

## How does it work?

When you run the script `youtube.py`, it saves the final file (depending on your menu choice) **on the current valid path from where the script was executed**. The videos are saved in an "*.mp4*" container whereas audio files are saved as "*.mp3*". Future updates will provide options for more customization. If the full video (or a section of it) is downloaded, the highest video and audio quality available are automatically chosen.

The logic of the procedures within this project makes sure the intended target (valid Youtube URL) seamlessly generates a valid final file downloaded locally on your machine so that only then operations can be done on it. This way, reinforcing the full separation between the download routine from any further necessary processing in order to generate the final file. 

The script temporarily saves a file named "*temp_video.mp4*" on the path from where the script is executed. Such file temporarily serves the application to perform further operations such as cutting and/or extracting audio/video. 

## Requirements

Script extensively tested on Python versions `3.10.0` and `3.10.2`. Pip was upgraded to version `pip 22.0.3`. 
*Creating a virtual environment for this project is optional but highly advisable since its changes will not have any effect on your local machine current settings.*

- Creating a virtual environment (optional)

```python
#creating the virtual environment
python -m venv <name_of_your_environment>

#activating the virtual environment
# - for unix systems
source <name_of_your_environment>/bin/activate
# - for windows systems
source <name_of_your_environment>/Scripts/activate

#upgrading pip
python -m pip install --upgrade pip
```

- Install the requirements

```python
pip install -r requirements.txt
```

## How to use this script?

1. Provide a valid Youtube URL
   - Youtube URL's are accepted: 
     - ht<area>tps://w<area>ww.youtube.com/watch?v={random_url}
     - ht<area>tp://ww<area>w.youtube.com/watch?v={random_url}
     - w<area>ww.youtube.com/watch?v={random_url}
     - youtube.com/watch?v={random_url}
     - {random_url}
2. Choose a menu option
   - If no arguments are passed after the Youtube URL, the script will download the full length of the video.

2. If you are cutting the video/audio, the time format used follows the logic `HH:MM:SS` (Hour, Minute, Second). For example:

   - 01:20:10 - At exactly 1 hour, 20 minutes and 10 seconds.

   - 00:01:30 - At exactly 1 minute and 30 seconds.

   - 00:00:15 - At exactly 15 seconds.

## Tips
- Some videos might take longer than others due to its length as well as your to your bandwidth
