#!/bin/bash

filename=$1
result=$(grep -E -c '\$TITLE\$|\$CONTENT\$|\$DESCRIPTION\$' $filename)
if [ $result -gt 0 ];
then
    echo "$result issue(s)"
    exit 1023
else
    echo 'success'
fi
