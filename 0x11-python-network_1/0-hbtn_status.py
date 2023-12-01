#!/usr/bin/python3
#fetches a url
import urllib.request
with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    page = response.read()
    print(page)
    