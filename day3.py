#! /usr/bin/env python3

with open('input3.txt') as f:
    data = f.read()

datarr = [line for line in data.strip().split('\n')]

dirs = [
    [-1,-1], [-1,0], [-1,1],
    [0,-1], [0,1],
    [1,-1], [1,0], [1,1]
]

def is_symbol(v):
    if v in '.1234567890':
        return False
    return True

def check_nbrs(datarr, y, x):
    symbol = False
    for dir in dirs:
        j,i = dir
        if j+y<0 or j+y>=len(datarr) or i+x<0 or i+x>=len(datarr[y]):
            continue
        if is_symbol(datarr[y+j][x+i]):
            symbol = True
            break
    return symbol

def get_number(datarr, y, x):
    return 0

sum = 0

y=0
while y<len(datarr):
    x=0
    while x<len(datarr[y]):
        if datarr[y][x].isdigit():
            isValid = check_nbrs(datarr, y, x)
            #print(datarr[y][x], isValid)
            if isValid:
                number = get_number(datarr, y, x)
            #sum+=int(number)
        x+=1
    y+=1
print(sum)
