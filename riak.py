#!/usr/bin/python

import requests
import sys
import os
from getssm import getSsmParams

def pushToRiak(riakUrl, riakFileName, unpacked):
    try:
        for root, dirs, files in os.walk(unpacked):
            for f in files:
                if f == riakFileName:
                    riakFile = root+"/"+f
        # req = requests.post(riakUrl, riakFile)
        # print(req.status_code)
        #return req.status_code
        print(riakUrl, riakFile)
    except Exception as e:
        print(e)

riakUrl = sys.argv[1]
riakFileName = sys.argv[2]
unpacked = sys.argv[3]
pushToRiak(riakUrl, riakFileName, unpacked)