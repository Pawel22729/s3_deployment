#!/usr/bin/python

import boto3
import sys
import logging

logging.basicConfig(level=logging.INFO)

def getSsmParams(path, region='eu-west-2'):
    try:
        cli = boto3.client('ssm', region_name=region)
        resp = cli.get_parameters_by_path(Path=path)
        params = {}
        for p in resp['Parameters']:
            params[p['Name'].split('/')[-1]] = p['Value']
            logging.info('Parameter found %s' % p['Name'].split('/')[-1])
        return params
    except Exception as e:
        print(e)