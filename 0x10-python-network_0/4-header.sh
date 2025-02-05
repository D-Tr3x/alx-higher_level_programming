#!/bin/bash
# Sends a GET request to a URL with `X-School-User-Id` header set to `98`
curl -sH "X-School-User-Id=98" "$1"
