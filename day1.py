#! /usr/bin/env python3
import string
import re

f = open("input1.txt", "r", encoding="utf-8")
lines = [l.strip() for l in f.readlines()]

#part 1
'''
sum = 0

for line in lines:
    fno = line.strip(string.ascii_letters)[0]
    lno = line.strip(string.ascii_letters)[-1]
    num = fno+lno
    num = int(num)
    sum+=num
#print(sum)
'''
#part 2
numbers_as_words = r"\b(?:one|two|three|four|five|six|seven|eight|nine)\b"
#numbers_as_digits = r"\b\d+\b"
pattern = re.compile(numbers_as_words, re.IGNORECASE)
for line in lines:
    matches = pattern.findall(line)
    if matches:
        print("line",line)
        print("matches",matches)
