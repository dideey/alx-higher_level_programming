#!/bin/bash
#sending post request and setting variables
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
