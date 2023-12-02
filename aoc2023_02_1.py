#!/usr/local/bin/python

import re

fh = open("input02_01.txt", "r")

games_sum = 0

for line in fh:
    possible = True
    turns = line.strip()
    re_turns = re.split(": |; |, ", turns)
    print(re_turns)
    for term in re_turns:
        if "blue" in term:
            bvalue = term.split()[0]
            if int(bvalue) > 14:
                possible = False
                break
        if "green" in term:
            gvalue = term.split()[0]
            if int(gvalue) > 13:
                possible = False
                break
        if "red" in term:
            rvalue = term.split()[0]
            if int(rvalue) > 12:
                possible = False
                break
        game_id = re_turns[0].split()[1]
    print(possible)
    if possible:
        games_sum += int(game_id)

print(games_sum)
