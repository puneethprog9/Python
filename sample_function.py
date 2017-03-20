#!/usr/bin/python
items=['banana','mango','apple','grapes',1,2,3,4.55,6]
def parse_lists(some_list):
    fruits=[]
    num=[]
    for i in some_list:
       if isinstance(i,int) or isinstance(i,float):
          num.append(i)
       elif isinstance(i,str):
           fruits.append(i)
       else:
            pass
    return fruits,num

print(parse_lists(items))
