#! /usr/bin/env python3

with open("input2.txt") as f:
    data = f.read()

colors = ["red", "green", "blue"]
lim = {"red": 12, "green": 13, "blue": 14}

invalid = []

for line in data.strip().split('\n'):
    id = int(line.split()[1][:-1])
    line = line.split(":")[1].strip()
    s = ""
    for c in line:
        if c!=" ":
            s+=c
    line = s
    i = 0
    while i<len(line):
        num = None
        if line[i].isdigit():
            if line[i+1].isdigit():
                num = int(line[i]+line[i+1])
                i+=1
            else:
                num = int(line[i])
            #print("num", num)
            for _, color in enumerate(colors):
                if line[i+1:i+1+len(color)]==color:
                    #print(color)
                    if num>lim[color]:
                        #print(num)
                        invalid.append(id)
                        break
        i+=1

all = set(range(1,101))
invalid = set(invalid)

valid = all.union(invalid) - all.intersection(invalid)
print(sum(valid))
