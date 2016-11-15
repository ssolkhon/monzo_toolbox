#!/usr/bin/env python
import requests
import shutil


def save_image_from_url(url, filename):
    try:
        response = requests.get(url, stream=True)
        with open(str(filename) + '.jpg', 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
        del response
        return True
    except Exception as e:
        print('Failed saving image (%s)' % url)
        raise e
