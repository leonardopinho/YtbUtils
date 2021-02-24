from pytube import YouTube
from moviepy.editor import *
from datetime import datetime
import os


class YtbUtils(object):
    @staticmethod
    def download(urls, convert_mp3=False):

        if urls is None or type(urls) is not list or len(urls) == 0:
            raise Exception('URLs parameter must be a list')

        result = False

        for i, url in enumerate(urls):
            try:
                now = datetime.now()
                timestamp = now.timestamp()
                filename = str(timestamp).replace('.', '_')
                file_movie = 'movie_{0}'.format(filename)

                youtube = YouTube(url)
                video = youtube.streams[0]
                video.download('./media/video', filename=file_movie)

                if convert_mp3:
                    movie = VideoFileClip(os.path.abspath('media/video/{0}}.mp4'.format(file_movie)))
                    movie.audio.write_audiofile(os.path.abspath('media/mp3/file_{0}.mp3'.format(filename)))

                result = True
            except Exception as e:
                raise Exception('Error when trying to download file: {0}'.format(e))

        return result
