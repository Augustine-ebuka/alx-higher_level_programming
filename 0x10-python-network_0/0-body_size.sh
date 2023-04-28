#!/bin/bash
# Get the byte size of the HTTP response header for a given URL
if [ $# -eq 0 ]; then
  echo "Error: URL not provided"
  exit 1
fi

# Send a GET request to the URL and store the response body in a variable
response=$(curl -s -o /dev/null -w "%{size_download}" "$1")

# Display the size of the response body in bytes
echo $response
