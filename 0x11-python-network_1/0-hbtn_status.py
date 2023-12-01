#!/usr/bin/python3
"""fetches a url"""
import urllib.request

if __name__ == "__main__":
    req = urllib.request.Request("https://alx-intranet.hbtn.io/status")
    with urllib.request.urlopen(req) as response:
        Page = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(Page)))
        print("\t- content: {}".format(Page))
        print("\t- utf8 content: {}".format(Page.decode("utf-8")))
