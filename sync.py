#!/usr/bin/python

import sys
import os
import datetime
import logging
import argparse
from getssm import getSsmParams

logging.basicConfig(level=logging.INFO)

def sync(location, bucket, product, cache_control='max-age=31556926', expires=31556926):
    try:
        params = getSsmParams('/group1/app1')
        cache_control = params['cache_control']
        expires = params['expires']
        logging.info('Params has been taken from ssm')
    except Exception as e:
        print("Can't get ssm params - params set to default")

    timeExpires = datetime.datetime.now() + datetime.timedelta(seconds=int(expires))
    timeExpires = timeExpires.strftime('%a, %d %b %Y %H:%M:%S GMT')
    logging.info('Expires date set to %s' % timeExpires)
    try:
        logging.info('Syncing...')
        os.system('''
            aws s3 sync --delete {location} s3://{bucket}/{product}/ \
                --cache-control {cache_control} \
                --expires "{expires}" \
            
            '''.format(location=location, bucket=bucket, product=product, cache_control=cache_control, expires=timeExpires))
        logging.info('Sync done')
    except Exception as e:
        print(e)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--location', required=True, help='location')
    parser.add_argument('-b', '--bucket', required=True, help='bucket name')
    parser.add_argument('-p', '--product', required=True, help='product = product bucket prefix')

    args = parser.parse_args()
    sync(args.location, args.bucket, args.product)