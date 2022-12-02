from pytube import YouTube
from pytube import Search
from pytube import Playlist

def download_song(link):
    """
    Download Youtube Link to audio and save onto output folder

    :param link: link to youtube video
    :type link: str
    :return: Nothing (Video downloads and is put in its own folder)
    :rtype: None
    """
    yt = YouTube(link)
    print(f"Downloading {yt.title}")
    stream = yt.streams.get_by_itag(140)
    stream.download()
    print("Finished")

def download_playlist(link):
    """
    Parse through all songs in playlist and download them

    :param link: link to youtube playlist
    :type link: str
    :return: Nothing (Videos are downloaded using the download_song function)
    :rtype: None
    """

    p = Playlist(link)
    for song in p.video_urls:
        download_song(song)


def link_search(term):
    """
    Search user term on Youtube and return a YouTube link

    :param term: user search
    :type term: str
    :return: Link to Youtube video
    :rtype: str
    """
    return f'https://youtu.be/{Search(term).results[0].video_id}'

