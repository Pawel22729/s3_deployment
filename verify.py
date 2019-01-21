#!/usr/bin/bash

import unittest
import boto3
import os

def verifyBucketContent(local_path, bucket):
    cli = boto3.client('s3')
    resp = cli.list_objects(bucket)
    remote_md5 = {}
    local_md5 = {}
    for remote in resp['Contents']:
        remote_md5[remote.split('/')[-1]] = remote['ETag']

    for root, dirs, files in os.walk(local_path):
        for f in files:
            if f == riakFileName:
                riakFile = root+"/"+f


class TestPipeline(unittest.TestCase):
    def test_sum(self):
        resp = suma(2,2)
        self.assertEqual(resp, 4)

if __name__ == '__main__':
    unittest.main()