#!/usr/bin/python3
# -*- coding: utf-8 -*-
""" script that takes in a URL, sends a request to the URL and displays the
body of the response.
"""
import requests
import sys
if __name__ == "__main__":
    if len(sys.argv) < 2:
        q = ""
    else:
        q = sys.argv[1]
    try:
        url = "http://0.0.0.0:5000/search_user"
        data = {"q": q}
        r = requests.post(url, data).json()
        if {"id", "name"} <= r.keys():
            print("[{}] {}".format(r['id'], r['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
