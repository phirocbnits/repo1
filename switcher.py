#!/usr/bin/env python3
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    if (y):
        return x/y
    else:
        return "invalid data"
def default(x,y):
    return "wrong option"
cased = {1:add,2:sub,3:mul,4:div}
print("1:add \n2:sub\n3:mul\n4:div")
c=int(input("enter your choice:"))
x,y=map(int,input("enter 2 num:").split())
print(cased.get(c,default)(x,y))

