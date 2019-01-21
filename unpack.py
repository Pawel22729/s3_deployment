#!/usr/bin/python

import zipfile
import tarfile
import os
import sys
import argparse
import logging
from getssm import getSsmParams

logging.basicConfig(level=logging.INFO)

def unpack(package, unpackTo):
    unpackDir = unpackTo
    os.makedirs(unpackDir)
    if package.endswith('.zip'):
        try:
            z = zipfile.ZipFile(package, 'r')
            z.extractall(unpackDir)
            logging.info('Unpacked to %s' % unpackDir)
        except Exception as e:
            print(e)
    elif package.endswith('.tar.gz'):
        try:
            t = tarfile.open(package, 'r')
            t.extractall(unpackDir)
            logging.info('Unpacked to %s' % unpackDir)
        except Exception as e:
            print(e)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--package', required=True, help='path to package [.zip / .tar.gz]')
    parser.add_argument('-u', '--unpack_to', required=True, help='unpack to')

    args = parser.parse_args()
    unpack(args.package, args.unpack_to)