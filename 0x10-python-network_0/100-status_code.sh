#!/bin/bash
# Sends a request to a URL, then displays only the status code of the response
curl -s -o /dev/null -w "%{http_code}" "$1"
