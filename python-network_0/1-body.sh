#!/bin/bash
# Printing request body if it is 200
response=$(curl -s -o /dev/null -w "%{http_code}" $1) && if [ $response -eq 200 ]; then echo $(curl -s $1); fi
