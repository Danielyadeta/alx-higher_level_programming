#!/usr/bin/python3
if __name__ == "__main__":
    import sys

len = len(sys.argv) - 1
sum = 0

for i in range(1, len + 1):
    sum = sum + int(sys.argv[i])

print("{:d}".format(sum))

