#!/bin/bash
# script that displays the size of the body of the response
curl -sI "$1" | grep -i "Allow" | awk -F ': ' '{print $2}'
