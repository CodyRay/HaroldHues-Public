#!/bin/bash

start='<background><starttime><year>2009</year><month>08</month><day>04</day><hour>00</hour><minute>00</minute><second>00</second></starttime>';
end='</background>';
static='<static><duration>1000.0</duration><file>%s</file></static>';
transition='<transition><duration>5.0</duration><from>%s</from><to>%s</to></transition>';

echo $start
echo 
prev_file='';
ls | grep -i -e .jpg -e .png | while read line
do
   file=$PWD/$line;
   if [[ $prev_file == '' ]]
   then
      printf $static "$file";
      echo 
   else
      printf $transition "$prev_file" "$file";
      echo 
      printf $static "$file";
      echo 
   fi 
   prev_file=$file;
done
echo $end
