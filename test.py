import unittest

from main import YtbDownload


class YtbDownloadTest(unittest.TestCase):

    def test_download_youtube_file(self):
        urls = [
            'https://www.youtube.com/watch?v=c_17jALtLbQ',
        ]
        result = YtbDownload.download(urls=urls)
        self.assertEqual(result, True)

    def test_download_stream_file(self):
        url = ''
        result = YtbDownload.download_file(url)
        self.assertIsNotNone(result)


if __name__ == '__main__':
    unittest.main()
