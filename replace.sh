#!/bin/bash
#
#author: Hailey Bureau
#latest edits: 28 April 2014
#

for DIR in `seq -w 01 1 10` 
do
  cd "$DIR"
  #begin loop to get into actual job directories and replace line 
  for VALUE in `seq -w 000 1 009`
  do
    cd "00$VALUE"
    sed -i "4s/walltime=250:00:00:00/walltime=72:00:00/" job.sh
    cd ../ 
  done
  #end for loop 2 
  cd ../
done 
#end for loop 1 
