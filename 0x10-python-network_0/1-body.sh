#!/bin/bash
# script that displays the size of the body of the response
curl -s -i -L "$1" | tail -n1
