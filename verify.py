#!/usr/bin/bash

import boto3
import os
import hashlib
import argparse

def verifyBucketContent(local_path, bucket, prefix):
    cli = boto3.client('s3')
    resp = cli.list_objects_v2(Bucket=bucket, Prefix=prefix)
    remote_md5 = {}
    for remote in resp['Contents']:
        remote_md5[remote['Key'].split('/')[-1].encode('utf-8')] = remote['ETag'].strip('"')

    local_md5 = {}
    for root, dirs, files in os.walk(local_path):
        for f in files:
            file_path = (root+"/"+f)
            with open(file_path, 'rb') as w:
                local_md5[f] = hashlib.md5(w.read()).hexdigest()

    return local_md5, remote_md5

if __name__ == '__main__': 
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--path', required=True, help='')
    parser.add_argument('-b', '--bucket', required=True, help='')
    parser.add_argument('-p', '--prefix', required=True, help='')
    args = parser.parse_args()

    local, remote = verifyBucketContent(args.path, args.bucket, args.prefix)
    if local == remote:
        print('MD5 verification pass...')
    else:
        raise Exception('MD5 verification failed')