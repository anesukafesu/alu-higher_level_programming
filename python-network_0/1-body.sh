#!/bin/bash
# Printing request body if it is 200
response=$(curl -s -o /dev/null -w "%{http_code}" "http://94fe1136c97d.57e96196.alu-cod.online:5000/") && if [ $response -eq 200 ]; then echo $(curl -s "http://94fe1136c97d.57e96196.alu-cod.online:5000/"); fi
