#!/bin/bash
# Takes in a URL and displays all HTTP methods accepted by the server
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
