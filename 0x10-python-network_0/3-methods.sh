#!/bin/bash
#dislapys all accepted methods
curl -sI "$1" | grep "Allow" | cut -d " " -f2-

