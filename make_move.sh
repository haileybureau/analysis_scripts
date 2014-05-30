#!/bin/bash

#author: Hailey Bureau 
#latest edits: 19 May 2014
#
# list all files with beginning frame.pdb. in the folder
for file in frame.pdb.*
do
   #build directories based on the # following .pdb; i'm honestly not sure how I got that to work but it did 
   #I think it splits the name of the file at the 10th character
   dir=${file:10:10}
   #makes the directories; i dont really know what -p does but it worked ok
   mkdir -p $dir
   # moves the corresponding file to the correct directory; again not really sure how it works; i think it's just luck
   mv $file $dir
done
