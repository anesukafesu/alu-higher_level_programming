#!/bin/bash
# Sending a get request to Holberton with a header
curl -s $1 -h 'X-HolbertonSchool-User-Id: 98'
