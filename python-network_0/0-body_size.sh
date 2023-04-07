#!/bin/bash
# 1. Makes a get request to whatever url is specified as the first arg
# 2. Gets the line with content length from the response using grep
# 3. Extracts the value field using cut
# 4. Removes any whitespaces before and after the actual value

curl -sI $1 | grep 'content-length' | cut -d ':' -f 2 | tr -d " "
