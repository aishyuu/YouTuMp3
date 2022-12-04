import sys
import argparse
import downloads
import filtering

parser = argparse.ArgumentParser(description="Download YouTube videos into a listenable Mp3 format")
parser.add_argument("-s", type=str, help="Download a single YouTube Video. (If using search term, 'type like this')")
parser.add_argument("-p", type=str, help="Download whole playlists given the link")
args = parser.parse_args()

def main():
    if len(sys.argv) > 1:
        #If the input does not start with 
        search = filtering.search(sys.argv[2])

        #Create new directory in "Results_Here" and set current directory to that
        filtering.create_and_set_dir()

        if args.s:
            downloads.download_song(search)
            sys.exit()

        if args.p:
            downloads.download_playlist(search)
            sys.exit()

    print("Please insert an option. Type -h for help")




if __name__ == "__main__":
    main()