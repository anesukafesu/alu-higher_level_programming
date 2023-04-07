#!/bin/bash
# Getting all the options a server accepts
curl -si -X OPTIONS $1 | grep 'Allow' | cut -d ':' -f 2 | xargs
