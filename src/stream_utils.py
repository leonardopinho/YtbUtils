import requests
import shutil


class StreamUtils(object):

    @staticmethod
    def download_file(url):
        if url is None:
            raise Exception('url is required')

        filename = 'media/video/{0}'.format(url.split('/')[-1])
        with requests.get(url, stream=True) as r:
            with open(filename, 'wb') as f:
                shutil.copyfileobj(r.raw, f)

        return filename
