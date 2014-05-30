set sel [atomselect top all]
set CA1 [atomselect top "resid 1 and name CA"]
set CA12 [atomselect top "resid 12 and name CA"]
set coords1 [$CA1 get {x y z}]
set coords2 [$CA12 get {x y z}]
set coords1m [vecinvert [expr $coords1]]
set M1 [transoffset $coords1m]
$sel move $M1
set coords2 [$CA12 get {x y z}]
set direct [vecnorm [expr $coords2]]
set M [transvecinv $direct]
$sel move $M
set M [transaxis y -90]
$sel move $M
[atomselect top all] writepdb 1LE0_frame10_imp.pdb
