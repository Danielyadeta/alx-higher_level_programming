#!/usr/bin/python3
if __name__ == "__main__":
    import sys

str = "argument"
len = len(sys.argv) - 1

if len > 1:
    str = str + "s"

if len != 0:
    print("{:d} {}:".format(len, str))
    for i in range(1, len + 1):
        print("{:d}: {}".format(i, sys.argv[i]))
else:
    print("0 arguments.")
