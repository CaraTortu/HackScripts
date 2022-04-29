#!/bin/bash
if [ $# -ne 1 ];then
   echo "Usage: bash brute-method.sh <input-file>"
   exit 1
fi

while read pass; do
    http_code=$(curl --write-out '%{http_code}' --silent --output /dev/null -X "$pass" http://10.10.85.204)
    if [ "$http_code" -ne 405 ] && [ "$http_code" -ne 501 ];then
        echo "SUCCESS: $pass"
        exit 0
    else
         echo "NOPE: $pass"
    fi

done < $1
