#!/bin/bash
#sends request to a specific url
curl -sL -X POST -H "Origin: NewSchool" -d "user_id=98" 0.0.0.0:5000/catch_me
