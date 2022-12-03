import sys
import argparse
import downloads
import os
from datetime import datetime
import re
from pytube import Search

parser = argparse.ArgumentParser(description="Download YouTube videos into a listenable Mp3 format")
parser.add_argument("-s", type=str, help="Download a single YouTube Video. (If using search term, 'type like this')")
parser.add_argument("-p", type=str, help="Download whole playlists given the link")
args = parser.parse_args()

def main():
    if len(sys.argv) > 1:
        #If the input does not start with 
        if not re.search(r"https?://(www\.)?youtube.com/", sys.argv[2]) and not re.search(r"https?://youtu\.be/", sys.argv[2]):
            #Search for the term on YouTube and grab the first results video id
            search = f'https://youtu.be/{Search(sys.argv[2]).results[0].video_id}'
        else:
            search = sys.argv[2]

        #Create new directory in "Results_Here" and set current directory to that
        date_string = str(datetime.now().strftime("%d_%m_%Y %H_%M_%S"))
        result_dir = os.getcwd()
        path = os.path.join(result_dir, "Results_Here" ,date_string)
        os.mkdir(path)
        os.chdir(path)

        if args.s:
            downloads.download_song(search)
            sys.exit()

        if args.p:
            downloads.download_playlist(search)
            sys.exit()

    print("Please insert an option. Type -h for help")




if __name__ == "__main__":
    main()