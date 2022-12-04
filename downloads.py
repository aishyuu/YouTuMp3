from pytube import YouTube
from pytube import Playlist

def download_song(link, gui):
    """
    Download Youtube Link to audio and save onto output folder

    :param link: link to youtube video
    :type link: str
    :param gui: If the current program is a gui or not
    :type gui: bool
    :return: Nothing (Video downloads and is put in its own folder)
    :rtype: None
    """
    yt = YouTube(link)
    print(f"Downloading {yt.title}")
    stream = yt.streams.get_by_itag(140)
    stream.download()
    print("Finished")

def download_playlist(link, gui):
    """
    Parse through all songs in playlist and download them

    :param link: link to youtube playlist
    :type link: str
    :return: Nothing (Videos are downloaded using the download_song function)
    :rtype: None
    """

    p = Playlist(link)
    if gui == True:
        for song in p.video_urls:
            download_song(song, True)

    else:
        for song in p.video_urls:
            download_song(song, False)

