# ytd

**Python script for downloading <u>[Youtube®](https://youtube.com)</u> videos at the highest video and audio quality.** 

## Features

- Download Youtube videos (Full length or sections)
- Download Youtube audio track (Full length or sections)

## How does it work?

The main script is `ytd.py`. It saves the final file (video or audio) through interactive or cli explicit parameters (context below on how to use this script). the final video or audio file is saved **on the current valid relative path where the script was executed**. The videos are saved in an "*.mp4*" container whereas audio files are saved as "*.mp3*". Future updates will provide options for more customization. If the full video (or a section of it) is downloaded, the highest video and audio quality available are automatically chosen.

The intended target (valid Youtube URL) seamlessly generates a valid final file downloaded locally on your machine so that only then operations can be done on it (trimming/cutting). A temporary file named "*temp_video.mp4*" is created on the current directory while the script is executed. This file is deleted at the end of its usage and script execution.

If no output file name is provided, the file will be named after the valid Youtube videl URL provided.

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

- You can also run it via Docker
```bash
# run this command from within the cloned repo locally (interactive script example)
docker run -it --rm --name ytdcontainer -v $(pwd)/:/ytd/  -w /ytd python:3.10.0 bash -c "pip install -r /ytd/requirements.txt && python /ytd/ytd.py"

# automated one liner example
docker run -it --rm --name ytdcontainer -v $(pwd)/:/ytd/  -w /ytd python:3.10.0 bash -c "pip install -r /ytd/requirements.txt && python /ytd/ytd.py --audio --url https://www.youtube.com/watch?v=An28cZyGZQI --start 00:00:20 --end 00:00:30 --output final"
```

## How to use this script?
### Interactive session

1. Provide a valid Youtube URL
   - Youtube URL's are accepted: 
     - ht<area>tps://w<area>ww.youtube.com/watch?v={random_url}
     - ht<area>tp://ww<area>w.youtube.com/watch?v={random_url}
     - w<area>ww.youtube.com/watch?v={random_url}
     - youtube.com/watch?v={random_url}
2. Choose a menu option
   - There are four options divided among audio and video. Both encompassing their full length or a section them.

3. If you are cutting the video/audio, the time format used follows the logic `HH:MM:SS` (Hour, Minute, Second). For example:

   - 01:20:10 - At exactly 1 hour, 20 minutes and 10 seconds.
   - 00:01:30 - At exactly 1 minute and 30 seconds.
   - 00:00:15 - At exactly 15 seconds.

### CLI parameters (Explicit arguments)
CLI parameters can also be used. This is fundamentally important when the commmand must be performed through automated routines. Available options:
- `--url/-u` - Provide Valid Youtube URL (required)
- `--video/-v` - Video stream (required)
- `--audio/-a` - Audio stream (required)
- `--start/-s` - Start point (required)
- `--end/-e` - End point (required)
- `--output/-o` - Output file name (without extension) (required)

Examples:
```bash
python ytd.py --url https://www.youtube.com/watch?v=f02mOEt11OQ --audio --start 00:00:10 --end 00:00:40 --output "Final file"
python ytd.py -u https://www.youtube.com/watch?v=f02mOEt11OQ --video --s 00:05:30 --end 00:10:50 -o "Middle Part"
```
The options can be shuffled without any problem. 

## Tips
- Some videos might take longer than others due to its length as well as your to your bandwidth.
- Make sure you check the releases for more up to date and consistent packages. 
- Executable file for Windows machines run regardless of any pre-existent software installation.
## Do you want to help?
- Contact me by e-mail at joaov777@gmail.com
