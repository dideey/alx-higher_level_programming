#!/bin/bash
#sends a json post request
curl -s -X POST -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
