## 
## Example script that sets the "User" data field with SASA values 
## 
## 
## Get list of residues (use 'residue' and not 'resid' so we don't get 
## duplicate residues from unusual PDB files..) 
##

##Latest edits: 28 May 2014
 
mol new 1893-2M60.psf type psf first 0 last -1 step 1 filebonds 1 \
        autobonds 1 waitfor all 
mol addfile 2m60-imp-smd2-gpu.dcd type dcd first 0 last -1 step 1 filebonds 1 \
        autobonds 1 waitfor all
set file [open "sasa_trajectory.txt" w]
set nf [molinfo top get numframes]
for {set i 0} {$i < $nf} {incr i} {
  set allsel [atomselect top all frame $i] 
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
    puts "residue $r, sasa: $rsasa, frame: $i"
    puts $file "$r $rsasa $i"
  } 
## 
## change the "color by" and "trajectory" tab settings to color by SASA 
## 
  mol modcolor 0 [molinfo top] User 
  mol colupdate 0 [molinfo top] 1 
  mol scaleminmax [molinfo top] 0 auto 
}
close $file 
