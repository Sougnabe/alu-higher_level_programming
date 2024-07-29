#!/bin/bash 
# display the length of the url only
curl -sI "$1" | grep 'Content-Length' | cut -d " " -f2
