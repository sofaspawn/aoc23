#! /usr/bin/env python3

with open('input3.txt') as f:
    data = f.read()

datarr = [line for line in data.strip().split('\n')]



dirs = [
    [-1,-1], [-1,0], [-1,1],
    [0,-1], [0,1],
    [1,-1], [1,0], [1,1]
]

y=0
while y<len(datarr):
    x=0
    while x<len(datarr[y]):
        if datarr[y][x].isdigit():
            number,i = getnumber(datarr, y, x)
            x+=i
            print(number)
        x+=1
    y+=1
