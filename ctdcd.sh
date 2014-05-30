#!/bin/bash
#
#authors: Alexandr Fonari and Hailey Bureau
#latest edits: July 2012
#
limits=(`jot - 1 10`)
str="vmd -psf ../0000-mainDir/00.psf"
for i in "${limits[@]}"
do
   dir_name=`printf "%02d" $i`
   ls=(`ls -l $dir_name | grep "^d" | awk '{print $9}'`)
   str=$str" -dcd "$dir_name"/"$ls"/"daOut.dcd
   
   # echo $dir_name
   # `ls $dir_name | head -1`
   # echo $i;
   # do whatever on $i
done

echo $str
