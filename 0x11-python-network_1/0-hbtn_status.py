#!/usr/bin/python3
"""
Prints different results of
a request
"""
import urllib.request


if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as response:
        html = response.read()
        print("Body response:")
        print("- type:", type(html))
        print("- content:", html)
        print("- utf8 content:", html.decode("utf-8"))
