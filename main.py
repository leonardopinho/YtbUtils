from pytube import YouTube
import shutil
import datetime
import math
from moviepy.editor import *
import os
import requests
import shutil


class YtbDownload(object):
    @staticmethod
    def download(urls):

        if type(urls) is not list or len(urls) == 0:
            raise Exception('URLs parameter must be a list')

        result = False

        for i, url in enumerate(urls):
            try:
                print(i)
                youtube = YouTube(url)
                video = youtube.streams[0]
                video.download('./files/video', filename='movie_{0}'.format(i))
                # movie = VideoFileClip(os.path.abspath("files/video/movie.mp4"))
                # movie.audio.write_audiofile(os.path.abspath("files/mp3/sound.mp3"))
                result = True
            except Exception as e:
                raise Exception('Error when trying to download file')

        return result

    @staticmethod
    def download_file(url):
        if url is None:
            raise Exception('url is required')

        filename = 'files/video/{0}'.format(url.split('/')[-1])
        with requests.get(url, stream=True) as r:
            with open(filename, 'wb') as f:
                shutil.copyfileobj(r.raw, f)

        return filename
