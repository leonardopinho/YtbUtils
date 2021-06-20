import unittest

from src.ytb_utils import YtbUtils
from src.stream_utils import StreamUtils


class YtbUtilsTest(unittest.TestCase):
    urls = [
        'https://www.youtube.com/watch?v=nbTq6QIeLAo',
    ]

    def test_download_youtube_file(self):
        result = YtbUtils.download(urls=self.urls, convert_mp3=False)
        self.assertEqual(result, True)

    def test_download_stream_file(self):
        url = '__url_here__'
        result = StreamUtils.download_file(url)
        self.assertIsNotNone(result)


if __name__ == '__main__':
    unittest.main()
