#!/bin/bash
# script that displays the size of the body of the response
curl -s -X OPTIONS -i "$1" | grep -i "Allow" | awk -F ': ' '{print $2}'
