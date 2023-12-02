#!/usr/local/bin/python

fh = open("input01.txt", "r")

calibration_values = []
two_digit = ""
first_digit = ""
last_digit = ""

for line in fh:
    
    for char in line:
        if char.isnumeric():
            first_digit = char
            print(first_digit)
            two_digit += char
            break
        else:
            continue

    for char in line[::-1]:
        if char.isnumeric():
            last_digit = char
            print(last_digit)
            two_digit += char
            print(two_digit)
            calibration_values.append(two_digit)
            two_digit = ""
            break
        else:
            continue

print(calibration_values)

summary = sum(map(int, calibration_values))

print(summary)
