#!/usr/bin/python

items=['banana','mango','apple','grapes',1,2,3,4.55,6]
fruits=[]
num=[]
for i in items:
    if isinstance(i,int) or isinstance(i,float):
       num.append(i)
    elif isinstance(i,str):
       fruits.append(i)
    else:
      pass

print(fruits)

print(num) 
