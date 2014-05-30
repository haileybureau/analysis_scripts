#author: Hailey Bureau 
#latest edits: 19 May 2014
#
set all [atomselect top all] 
set fixatom [atomselect top "protein"] 
$all set beta 0 
$fixatom set beta 1 
$all set occupancy 0
$all writepdb fixed.pdb
