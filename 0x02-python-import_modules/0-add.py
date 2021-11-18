#!/usr/bin/python3
if __name__ == "__main__":
    from add_0 import add as add_f

    a = 1
    b = 2

    c = add_f(a, b)

    print("{:d} + {:d} = {:d}".format(a, b, c))
