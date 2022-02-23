# ytd
Python script for dowloading Youtube videos at the highest video and audio quality. 

## Features
- Dowload full length Youtube videos at the highest quality available.
- Download either full or part of both audios and/or videos.
- Cut parts of a video stored locally on your machine.
- Both download and cut part of a Youtube video at once.

## Requirements
Script extensively tested on `python 3.10.2` and on `pip 22.0.3`. 
*Creating a Python virtual environment for the execution of this project is optional but highly advisable since its changes and requirements will not have any effect on your local machine current settings.*
- Creating a virtual environment

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

Install the requirements
```python
pip install -r requirements.txt
```

## How to use this script?
1. Time format must be inserted into the script following the logic described `HH:MM:SS` (Hour, Minute, Second). For example:
- 01:20:10 - At exactly 1 hour, 20 minutes and 10 seconds.
- 00:01:30 - At exactly 1 minute and 30 seconds.

