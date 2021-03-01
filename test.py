import unittest

from src.ytb_utils import YtbUtils
from src.stream_utils import StreamUtils


class YtbUtilsTest(unittest.TestCase):
    urls = [
        'https://www.youtube.com/watch?v=57KRiqDa7jI',
        'https://www.youtube.com/watch?v=zHnXxt-4nPI',
        'https://www.youtube.com/watch?v=q1EV_5U6GGo',
        'https://www.youtube.com/watch?v=AotIQzCZrwo',
        'https://www.youtube.com/watch?v=WrWSzUh7aRQ',
    ]

    def test_download_youtube_file(self):
        result = YtbUtils.download(urls=self.urls, convert_mp3=True)
        self.assertEqual(result, True)

    def test_download_stream_file(self):
        url = '__url_here__'
        result = StreamUtils.download_file(url)
        self.assertIsNotNone(result)


if __name__ == '__main__':
    unittest.main()
