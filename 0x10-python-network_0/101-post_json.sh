#!/bin/bash
# sends JSON POST request to URL passed as first arg, display body of response.
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
