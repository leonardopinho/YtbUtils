import unittest

from src.ytb_utils import YtbUtils
from src.stream_utils import StreamUtils


class YtbUtilsTest(unittest.TestCase):
    urls = [
        'https://www.youtube.com/watch?v=57KRiqDa7jI',
    ]

    def test_download_youtube_file(self):
        result = YtbUtils.download(urls=self.urls)
        self.assertEqual(result, True)

    def test_download_stream_file(self):
        url = '__url_here__'
        result = StreamUtils.download_file(url)
        self.assertIsNotNone(result)


if __name__ == '__main__':
    unittest.main()
