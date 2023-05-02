#!/usr/bin/env bash
#  takes in a URL, sends a request to that URL, and displays the size of the body of the response

response=$(curl -s -w "\n%{size_download}" "$1")
size=$(echo "$response" | tail -n2)
echo "$size"
