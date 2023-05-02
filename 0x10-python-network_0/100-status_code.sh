#!/bin/bash
#this real a url  and echo the atatus to the url
read  url
curl -I -s -o /dev/null -w "%{http_code}" $url

