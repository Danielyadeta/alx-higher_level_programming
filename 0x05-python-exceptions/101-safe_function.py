#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        r = fct(*args)
        return r
    except Exception as e:
        sys.stderr.write("Exception: %s\n" % e)
        # print("Exception: {}".format(e), file=sys.stderr)
        return None
