""" Class required for playing music through Athena"""

import os

import playsound
import yt_dlp as youtube_dl


class MusicPlayer:
    """
    Username of user on spotify
    Client ID and secret ID for the developer app created
    """

    # TODO: ADD SPOTIFY FUNCTIONALITY

    def __init__(self) -> None:
        self.ydl_opts = {
            "format": "bestaudio/best",
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "192",
                }
            ],
            "ffmpeg_location": "C:\\Windows\\YOUTUBE_DL",
        }

    def play_yt(self, query):
        # TODO: MAKE ASYNC
        """Downloads a song from youtube that matches the query, plays it then deletes it"""
        with youtube_dl.YoutubeDL(self.ydl_opts) as ydl:
            os.chdir(
                "C:/Users/adnan/Dropbox/Coding Projects/Python/AI/Athena/extras/CachedMusic"
            )
            info = ydl.extract_info(f"ytsearch:{query}")
            file_name = f"{info.get('entries')[0]['title']} [{info.get('entries')[0]['id']}].mp3"

            playsound.playsound(file_name)
            os.remove(file_name)
