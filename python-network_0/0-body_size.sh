#!/bin/bash

curl -sI $1 | grep 'content-length' | cut -d ':' -f 2 | tr -d " "
