import re
from pytube import Search
from datetime import datetime
import os

def search(user_search):
    if not re.search(r"https?://(www\.)?youtube.com/", user_search) and not re.search(r"https?://youtu\.be/", user_search):
        #Search for the term on YouTube and grab the first results video id
        return f'https://youtu.be/{Search(user_search).results[0].video_id}'
    else:
        return user_search

def create_and_set_dir():
    date_string = str(datetime.now().strftime("%d_%m_%Y %H_%M_%S"))
    result_dir = os.getcwd()
    path = os.path.join(result_dir, "Results_Here" ,date_string)
    os.mkdir(path)
    os.chdir(path)