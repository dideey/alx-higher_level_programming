#!/usr/bin/python3
"""fetches a url"""
import urllib.request

if __name__ == "__main__":

    req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    with urllib.request.urlopen(req) as re:
        page = re.read()

        print("Body response:")
        print("\t-type: {}".format(type(page)))
        print("\t-content: {}".format(page))
        print("\t-utf8 content: {}".format(page.decode("utf-8")))