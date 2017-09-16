#!/usr/bin/python

import time
import json

date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 
print json.dumps({
    "time" : date
})
