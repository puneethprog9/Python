#!/usr/bin/python

def some_func(arg1,arg2,karg1=None,karg2=None):
    print(arg1,arg2)
    if karg1 != None:
       print(karg1)



some_func('abc','car',karg1='not a big deal')
