#!/usr/bin/python3
# -*- coding: utf-8 -*-
""" script that fetches https://intranet.hbtn.io/status with request
"""
import requests
if __name__ == "__main__":
    r = requests.get('https://intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))
