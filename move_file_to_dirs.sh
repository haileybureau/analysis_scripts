#!/bin/bash
#
#author: Hailey Bureau 
#latest edits: 19 May 2014
#
for dir in *; do [ -d "$dir" ] && cp job.sh  "$dir" ; done
