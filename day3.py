#! /usr/bin/env python3

with open('input3.txt') as f:
    data = f.read()

datarr = [line for line in data.strip().split('\n')]

def getnumber(datarr, y, x):
    s = ""
    i = 0
    while datarr[y][x+i].isdigit():
        s+=datarr[y][x+i]
        i+=1
    return int(s),i

y=0
x=0

while y<len(datarr):
    while x<len(datarr[y]):
        if datarr[y][x].isdigit():
            number,i = getnumber(datarr, y, x)
            x+=i
            print(number)
        x+=1
    y+=1
    break
