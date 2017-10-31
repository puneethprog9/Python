#!/usr/bin/python3

import requests as req
import re

resp = req.get("http://www.puneethaws.com")

content = resp.text

stripped = re.sub('<.*?>','', content)

stripped = re.sub('\n','',stripped)
stripped = re.sub('\s','',stripped)
print(stripped)

