#!/usr/bin/python

import requests as req
import re

site=req.get('https://blacked.com')

strip=re.search('https:\/\/[a-z0-9A-Z-.\/_]*jpg',site.text)

print(strip.groups(0))
