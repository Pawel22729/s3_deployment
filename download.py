#!/usr/bin/python

import requests
import sys
import logging
import argparse
from getssm import getSsmParams

logging.basicConfig(level=logging.INFO)

def getFile(url, saveAs):
    try:
        logging.info('Downloading...')
        req = requests.get(url)
        fileName = saveAs
        if url.endswith('.zip'):
            fileName += '.zip'
        elif url.endswith('tar.gz'):
            fileName += '.tar.gz'
        with open(fileName, 'wb') as f:
            f.write(req.content)
        logging.info('Download saved as %s' % fileName)
    except Exception as e:
        return e

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--url', required=True, help='package url [.zip / .tar.gz]')
    parser.add_argument('-s', '--save_as', default='application_package', help='save as')

    args = parser.parse_args()
    getFile(args.url, args.save_as)