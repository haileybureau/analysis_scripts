#!/bin/bash
#
#author: Hailey Bureau 
#latest edits: 19 May 2014
#
#
vmd="/Applications/VMD 1.9.1.app/Contents/Resources/VMD.app/Contents/MacOS/VMD"
#
#list all directories only by listing only that which ends with '/' which is always directories 
for dir in $(ls -d */); do
    #dir1 holds only the actual name of the directory; i.e. 785 instead of 785/
    dir1=${dir%?}
    #echo $dir1
    #copy the file whhose path is, for example, 785/frame.pdb.785 to 785/frame.pdb
    cp "${dir1}/frame.pdb.${dir1}" "${dir1}/frame.pdb.tmp"
    #replace the last column of frame.pdb to have 6 spaces and BH
    head -n 104 "${dir1}/frame.pdb.tmp" | cut -c 1-66 | sed -e 's/$/      BH/' > "${dir1}/frame.pdb"
    #tried softlinking but didn't need to
    #ln -s ./solvate.tcl ./${dir1}/
    #enter directory
    cd $dir1
    #removing tcl files from each directory because I will run them from top directory anyway
    rm -f solvate.tcl
    rm -f set_fixedatoms.tcl
    rm -f measure.tcl
    #run all tcl scripts 
    "$vmd" -eofexit -dispdev text < ../solvate.tcl
    "$vmd" -eofexit -dispdev text < ../set_fixedatoms.tcl
    "$vmd" -eofexit -dispdev text < ../measure.tcl
    
    #replace the appropriate cell basis vectors in the .conf file with the calculated in the cell_basis_vector.dat file 
    #create the temp var for the entire value 
    cbv1tmp=$(awk '{print $1}' cell_basis_vectors.dat)
    #cut only the first 6 values from the temp var
    cbv1=${cbv1tmp:0:6}
    cbv2tmp=$(awk '{print $2}' cell_basis_vectors.dat)
    cbv2=${cbv2tmp:0:6}
    cbv3tmp=$(awk '{print $3}' cell_basis_vectors.dat)
    cbv3=${cbv3tmp:0:6}
    #replace the cbv vars from the .conf file with the cut string #'s 
    sed -i '' "s/cbvx/${cbv1}/g" equilibration_100ps.conf
    sed -i '' "s/cbvy/${cbv2}/g" equilibration_100ps.conf
    sed -i '' "s/cbvz/${cbv3}/g" equilibration_100ps.conf
    #echo $cbv1
    
    #replace the appropriate cell origin values in the .conf file with the calculated in the cell_origin.dat file 
    #create the temp var for the entire value 
    co1tmp=$(awk '{print $1}' cell_origin.dat)
    #cut only the first 6 values from the temp var
    co1=${co1tmp:0:6}
    co2tmp=$(awk '{print $2}' cell_origin.dat)
    co2=${co2tmp:0:6}
    co3tmp=$(awk '{print $3}' cell_origin.dat)
    co3=${co3tmp:0:6}
    #replace the cbv vars from the .conf file with the cut string #'s 
    sed -i '' "s/cox/${co1}/g" equilibration_100ps.conf
    sed -i '' "s/coy/${co2}/g" equilibration_100ps.conf
    sed -i '' "s/coz/${co3}/g" equilibration_100ps.conf
    cd ../
done
