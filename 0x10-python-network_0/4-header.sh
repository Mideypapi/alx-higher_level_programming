#!/bin/bash
# takes URL, sends GET to the URL, and displays the body of the response
curl -sLH 'X-HolbertonSchool-User-Id:98' "$1"
