##
## borrowed from online
## 2 May 2014
## 
## Example script that sets the "User" data field with SASA values 
## 
## 
## Get list of residues (use 'residue' and not 'resid' so we don't get 
## duplicate residues from unusual PDB files..) 
## 
set file [open "sasa_trajectory" w]
set nf [molinfo top get numframes]
for {set i 0} {$i < $nf} {incr i} {
  set allsel [atomselect top protein frame $i] 
  set residlist [lsort -unique [$allsel get residue]] 
## 
## Make an atom selection, set the User field with the SASA value for 
## the selected atom 
## 
  foreach r $residlist { 
    set sel [atomselect top "residue $r"] 
    set rsasa [measure sasa 1.4 $allsel -restrict $sel] 
    $sel set user $rsasa 
    #$sel delete 
    puts "residue $r, sasa: $rsasa"
    puts $file $rsasa 
  } 
## 
## change the "color by" and "trajectory" tab settings to color by SASA 
## 
  mol modcolor 0 [molinfo top] User 
  mol colupdate 0 [molinfo top] 1 
  mol scaleminmax [molinfo top] 0 auto 
}
close $file 
