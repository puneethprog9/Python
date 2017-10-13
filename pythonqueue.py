#!/usr/bin/python

import time 
import  multiprocessing 

def fn_sqrt(numbers,q):
    for n in numbers:
        q.put(n*n)

if __name__ == "__main__":

   arr=[2,3,4,5]

   q = multiprocessing.Queue()

   p1=multiprocessing.Process(target=fn_sqrt,args=(arr,q))

   p1.start()

   p1.join()

while q.empty() is False:
      print(q.get())
