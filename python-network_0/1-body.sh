#!/bin/bash
# Printing request body if it is 200
response=$(curl -sL -o /dev/null -w "%{http_code}" $1) && if [ $response -eq 200 ]; then printf "$(curl -sL $1)"; fi
