#!/usr/bin/python

import requests

test = requests.get('http://www.google.com')

outfile = open('/root/Python/google.html','w')

outfile.write(test.text.encode('utf-8'))

print(test.headers)
