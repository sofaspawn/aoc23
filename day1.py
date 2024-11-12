#! /usr/bin/env python3

import string

f = open("input1.txt", "r")
lines = [l.strip() for l in f.readlines()]

sum = 0

for line in lines:
    fno = line.strip(string.ascii_letters)[0]
    lno = line.strip(string.ascii_letters)[-1]
    num = fno+lno
    num = int(num)
    sum+=num

#print(sum)

#part 2
