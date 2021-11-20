#!/usr/bin/python3
delim = ", "
for i in range(0, 100):
    if i == 99:
        delim = ""

    print("{:02d}".format(i), end=delim)

print()
