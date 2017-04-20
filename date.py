#!/usr/bin/python

import datetime

today=datetime.date.today()

text="{today.month}/{today.year}/{today.day}".format(today=today)



print(today)

print(text)
