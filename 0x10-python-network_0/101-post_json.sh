#!/bin/bash
# script that displays the size of the body of the response
curl -s -d "$2" -H "Content-Type: application/json" -X POST "$1"
