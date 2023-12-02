#!/usr/local/bin/python

fh = open("input01.txt", "r")

calibration_values = []
two_digit = ""
first_digit = ""
last_digit = ""
dict_digit = {"one":"1","two":"2","three":"3","four":"4","five":"5","six":"6","seven":"7","eight":"8","nine":"9"}
test_string_L = ""
test_string_R = ""

for line in fh:
    test_string_L = ""
    test_string_R = ""
    for alpha in line: # check for substring from left
        test_string_L += alpha
        print(test_string_L)
        for key in dict_digit.keys():
            if key in test_string_L:
                line = line.replace(key, dict_digit[key])
                print(key)
                print(line)
                break
            elif alpha.isnumeric():
                break
        if key in test_string_L or alpha.isnumeric(): break    

    for beta in line[::-1]: # check for substring from right
        test_string_R = beta + test_string_R
        print(test_string_R)
        for key in dict_digit.keys():
            if key in test_string_R:
                line = line.replace(key, dict_digit[key])
                print(key)
                print(line)
                break
            elif beta.isnumeric():
                break
        if key in test_string_R or beta.isnumeric(): break    
                
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
