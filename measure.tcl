#
#author: Hailey Bureau 
#latest edits: 19 May 2014
#
mol new solvate.pdb
set all [atomselect top all]

#set file for output of the cell basis vectors
set file [open "myoutput.dat" w]
#measure vectors with radii of atoms
set minmax [measure minmax $all -withradii]
#add those vectors together and scale by 1.1
set box [vecscale 1.1 [vecsub [lindex $minmax 1] [lindex $minmax 0]]]
#set test [vecadd [lindex $minmax 0] [lindex $minmax 1]]
#puts $test
#write the total vector to the output file 
puts $file $box
#puts $file [ measure center $all ]

close $file
