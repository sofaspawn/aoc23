#! /usr/bin/env python3

f = open("input.txt", "r")
for line in f.readlines():
    line.strip()
    print(line)
