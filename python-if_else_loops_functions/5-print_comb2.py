#!/usr/bin/python3

for i in range(100):
    output = "0" if i < 10 else ""
    output += str(i)
    output += "\n" if i == 99 else ", "
    print(output, end="")
