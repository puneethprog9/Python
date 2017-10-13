#!/usr/bin/python

import time 
from  multiprocessing import Process

def fn_sqrt(numbers):
    for n in numbers:
        time.sleep(0.2)
        print("square",n*n)


def fn_cube(numbers):
    for n in numbers:
        time.sleep(0.2)
        print("cube",n*n*n)

if __name__ == "__main__":
   arr=[2,3,4,5]


   t1=Process(target=fn_sqrt,args=(arr,))

   t2=Process(target=fn_cube,args=(arr,))

   t1.start()

   t2.start()

   t1.join()

   t2.join()


