#!/usr/bin/env python
#
# 11-Feb-2015 v1.0 initial script
# this file - 
#

import sys
import time
import socket
import os

from twython import Twython

# Define location of api files - recorded in a file - avoids a GitHub slurp for API keys!
keys_file='/home/pi/Desktop/twitter_api_key.txt'

# Read API keys from file
with open(keys_file) as f:
    CONSUMER_KEY = f.readline().strip("\n")
    CONSUMER_SECRET = f.readline().strip("\n")
    ACCESS_KEY = f.readline().strip("\n")
    ACCESS_SECRET = f.readline().strip("\n")

# Post tweet
api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)
#api.update_status(status="<->")
