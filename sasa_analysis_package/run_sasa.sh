#!/bin/bash

## Author: Hailey Bureau 
## Latest edits: 28 May 2014

#calls vmd --this is where you might need to edit for your executable location
vmd="/Applications/VMD 1.9.1.app/Contents/Resources/VMD.app/Contents/MacOS/VMD"

#calls vmd to run new_sasa_trajectory.tcl
"$vmd" -eofexit -dispdev text < new_sasa_trajectory.tcl

#loops through all 43 residues
for x in {0..42}; do
  #adds one to variable x to get what the "real" residue index is
  realnum=$[x + 1]
  #greps the sasa_trajectory.txt file for the residue and writes out individual files for each residue
  grep "^$x " sasa_trajectory.txt > "${realnum}residue.txt"
done
