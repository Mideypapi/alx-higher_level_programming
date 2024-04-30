#!/bin/bash
# sends DELETE to URL passed and displays the body of the response
curl -s "$1" -X DELETE
