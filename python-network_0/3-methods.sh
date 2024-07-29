#!/bin/bash
#display all the allowed methods 
curl -sI "$1" | grep "Allow: " | cut -d " " -f 2-
