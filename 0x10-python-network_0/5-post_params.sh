#!/bin/bash
# script that displays the size of the body of the response
curl -s -d "email='test@gmail.com'&subject='I will always be here for PLD'" -X POST "$1"
