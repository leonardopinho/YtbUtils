import unittest

from src.ytb_utils import YtbUtils
from src.stream_utils import StreamUtils


class YtbDownloadTest(unittest.TestCase):
    urls = [
        'https://www.youtube.com/watch?v=c_17jALtLbQ',
    ]

    def test_download_youtube_file(self):
        result = YtbUtils.download(urls=self.urls)
        self.assertEqual(result, True)

    def test_download_stream_file(self):
        url = ''
        result = StreamUtils.download_file(url)
        self.assertIsNotNone(result)


if __name__ == '__main__':
    unittest.main()
