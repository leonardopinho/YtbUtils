from pytube import YouTube
from moviepy.editor import *
import os


class YtbUtils(object):
    @staticmethod
    def download(urls, convert_mp3=False):

        if type(urls) is not list or len(urls) == 0:
            raise Exception('URLs parameter must be a list')

        result = False

        for i, url in enumerate(urls):
            try:
                youtube = YouTube(url)
                video = youtube.streams[0]
                video.download('./media/video', filename='movie_{0}'.format(i))

                if convert_mp3:
                    movie = VideoFileClip(os.path.abspath("media/video/movie.mp4"))
                    movie.audio.write_audiofile(os.path.abspath("media/mp3/sound.mp3"))

                result = True
            except Exception as e:
                raise Exception('Error when trying to download file')

        return result
