#!/bin/bash
# Send a request to a URL for a response with a message containing 'You got me!'
curl -sL -X PUT -H "Origin: School" 0.0.0.0:5000/catch_me
