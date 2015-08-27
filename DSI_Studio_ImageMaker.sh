#!/bin/bash

#This script is for reading in the dsi-studio text files and saving just the column of actual numbers.
#make sure  all your subs are located in the same directory with similar names and NO WH ITE SPACE.
# comment out below for the tracts you want to plot
declare -a Tracts=( "Callosum.trk.txt"\
"Frontal_Pole.trk.txt" \
# "CallosalFrontal.trk.txt" \
# "CallosalPosterior.trk.txt" \
"VerticalFrontal.trk.txt" \
# "MotorTract.trk.txt"
"L_Cingulum.trk.txt" \
"L_FrontoThalamic.trk.txt" \
##"L_Uncinate_Fasciculus.trk.txt" \
# "L_IFOF.trk.txt" \
# "L_Arcuate.trk.txt"  
# "L_ShortAssociation.trk.txt" \
"R_Cingulum.trk.txt" \
"R_FrontoThalamic.trk.txt" \
"R_Uncinate_Fasciculus.trk.txt" )
# "R_IFOF.trk.txt" \
# "R_Arcuate.trk.txt" \
# "R_ShortAssociation.trk.txt")


#set your loop to go through all the directories that match the wildcard format given below, or just be lazy and put in the subs name
for s in *_Guys
do
	cd $s #go into the sub directory

	sub=${PWD##*/} #get the subs dir name for the file name to be saved
	for f in "${Tracts[@]}"
	do 
		if [[ $f == R* ]]
			then
			#make right hemi fibers
			dsi_studio --action=vis --source=IXI$s.dti.fib.gz --track=$f --cmd="add_slice,t1.bfc.nii.gz;slice_off,1;slice_off,1;set_view,0;save_image,$f.jpg"
		elif [[ $f == L* ]]
			then
			#Make a left hemi fiber. 
			dsi_studio --action=vis --source=IXI$s.dti.fib.gz --track=$f --cmd="add_slice,t1.bfc.nii.gz;slice_off,1;slice_off,1;set_view,0;set_view,0;save_image,$f.jpg"
		else
			#make right hemi fibers
			dsi_studio --action=vis --source=IXI$s.dti.fib.gz --track=$f --cmd="add_slice,t1.bfc.nii.gz;slice_off,1;slice_off,2;set_view,0;save_image,$f.jpg"
		fi 
	done	
	cd ../ #bump back up a directory to the main one--a bit of a hack
done

#rename all the .trk.txt.jpgs to just .jpgs; a bit of a hack.
for s in *Guys
do
	cd $s
	for file in *.trk.txt.jpg
	do
		mv "$file" "`basename $file .trk.txt.jpg`.jpg"
	done
	cd ../
done



