#!/usr/bin/python

import time 
import threading

def fn_sqrt(numbers):
    for n in numbers:
        time.sleep(0.2)
        print("square",n*n)


def fn_cube(numbers):
    for n in numbers:
        time.sleep(0.2)
        print("cube",n*n*n)


arr=[2,3,4,5]

t=time.time()

t1=threading.Thread(target=fn_sqrt,args=(arr,))

t2=threading.Thread(target=fn_cube,args=(arr,))

t1.start()

t2.start()

t1.join()

t2.join()


print("done in :",time.time()-t)
