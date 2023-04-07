#!/bin/bash
# Makes a get request to whatever url is specified as the first arg, gets the line with content length from the response using grep, extracts the value field using cut, removes any whitespaces before and after the actual value
curl -sI $1 | grep 'Content-Length' | cut -d ':' -f 2 | tr -d " "
