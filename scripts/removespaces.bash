#!/bin/bash

ls | grep '[a-zA-Z0-9]\ [a-zA-Z0-9]' | while read line 
do
mv "$line" $( echo $line | sed s/' '/'_'/g )
done
