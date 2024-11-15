#! /usr/bin/env python3
import string

#f = open("input1.txt", "r", encoding="utf-8")
#lines = [l.strip() for l in f.readlines()]

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
'''
nums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
ans = 0
for line in lines:
    first = 0
    last = 0

    for i in range(len(line)):
        curr = None
        if line[i].isdigit():
            curr = int(line[i])

        for j, num in enumerate(nums):
            if line[i:i+len(num)] == num:
                curr = j+1
                break
        if curr:
            if first is None:
                first = curr
            last = curr

    ans+=first*10+last
print(ans)
'''

with open("input1.txt") as fin:
    data = fin.read()

ans = 0
nums = ["one", "two", "three", "four", "five",
        "six", "seven", "eight", "nine"]

for line in data.strip().split():
    first = None
    last = None

    for i in range(len(line)):
        cur = None

        c = line[i]
        if c.isdigit():
            cur = int(c)

        for j, num in enumerate(nums):
            if line[i:(i+len(num))] == num:
                cur = j + 1
                break

        if cur:
            if first == None:
                first = cur
            last = cur

    ans += first * 10 + last

print(ans)
