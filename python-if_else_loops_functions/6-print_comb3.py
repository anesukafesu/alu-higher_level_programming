#!/usr/bin/python3

for i in range(9):
    for j in range(i + 1, 10):
        output = str(i) + str(j)
        output += "\n" if output == "89" else ", "
        print("{}".format(output), end="")
