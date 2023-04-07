#!/bin/bash
# Getting all the options a server accepts
curl -si -X OPTIONS http://94fe1136c97d.57e96196.alu-cod.online:5000 | grep 'Allow' | cut -d ':' -f 2 | xargs
