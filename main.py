from pytube import YouTube
import shutil
import datetime
import math
from moviepy.editor import *
import os

try:
    url = 'https://www.youtube.com/watch?v=zHnXxt-4nPI'

    youtube = YouTube(url)
    video = youtube.streams.first()
    video.download('./files/video', filename='movie')
    movie = VideoFileClip(os.path.abspath("files/video/movie.mp4"))
    movie.audio.write_audiofile(os.path.abspath("files/mp3/sound.mp3"))

    print('end')
except Exception as e:
    print(e)
