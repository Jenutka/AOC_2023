#!/usr/local/bin/python

import re

fh = open("input02_01.txt", "r")

games_sum = 0

for line in fh:
    blue = []
    green = []
    red = []
    turns = line.strip()
    re_turns = re.split(": |; |, ", turns)
    print(re_turns)
    for term in re_turns:
        if "blue" in term:
            bvalue = term.split()[0]
            blue.append(int(bvalue))
        if "green" in term:
            gvalue = term.split()[0]
            green.append(int(gvalue))
        if "red" in term:
            rvalue = term.split()[0]
            red.append(int(rvalue))
    print(max(blue))
    print(max(green))
    print(max(red))
    power = max(blue) * max(green) * max(red)
    print(power)
    games_sum += power

print(games_sum)
