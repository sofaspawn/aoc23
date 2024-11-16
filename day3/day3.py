#! /usr/bin/env python3
'''
with open('day3/ex3.txt') as f:
    data = f.read()
'''
with open('day3/input3.txt') as f:
    data = f.read()

datarr = [line for line in data.strip().split('\n')]

dirs = [
    [-1,-1], [-1,0], [-1,1],
    [0,-1], [0,1],
    [1,-1], [1,0], [1,1]
]

def is_symbol(v):
    return v not in ".0123456789"

def check_nbrs(datarr, y, x):
    symbol = False
    for dir in dirs:
        j,i = dir
        if j+y<0 or j+y>=len(datarr) or i+x<0 or i+x>=len(datarr[y]):
            continue
        if is_symbol(datarr[y+j][x+i]):
            symbol = True
            #break
    return symbol

sum = 0

y=0
while y<len(datarr):
    curr = ""
    curr_is_valid = False
    x=0
    while x<len(datarr[y]):
        if datarr[y][x].isdigit():
            curr+=datarr[y][x]
            valid = check_nbrs(datarr, y, x)
            if valid and not curr_is_valid:
                curr_is_valid = True
            #print(datarr[y][x], isValid)
        else:
            if curr_is_valid:
                print(curr)
                sum+=int(curr)
            curr=""
            curr_is_valid = False
        x+=1
    y+=1
print(sum)
