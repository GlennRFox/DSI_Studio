#!/bin/bash

#This script is for reading in the dsi-studio text files and saving just the column of actual numbers.
#make sure  all your subs are located in the same directory with similar names and NO WH ITE SPACE
declare -a Tracts=("Callosum.trk.txt.statistics.txt" \
"Frontal_Pole.trk.txt.statistics.txt" \
"CallosalFrontal.trk.txt.statistics.txt"\ 
"CallosalPosterior.trk.txt.statistics.txt"\ 
"VerticalFrontal.trk.txt.statistics.txt" \
"MotorTract.trk.txt.statistics.txt"
"L_Cingulum.trk.txt.statistics.txt" \
"L_FrontoThalamic.trk.txt.statistics.txt"\ 
"L_Uncinate_Fasciculus.trk.txt.statistics.txt"\ 
"L_IFOF.trk.txt.statistics.txt" \
"L_Arcuate.trk.txt.statistics.txt"\ 
"L_ShortAssociation.trk.txt.statistics.txt"\ 
"R_Cingulum.trk.txt.statistics.txt" \
"R_FrontoThalamic.trk.txt.statistics.txt" \
"R_Uncinate_Fasciculus.trk.txt.statistics.txt"\ 
"R_IFOF.trk.txt.statistics.txt" \
"R_Arcuate.trk.txt.statistics.txt"\ 
"R_ShortAssociation.trk.txt.statistics.txt")



#set your loop to go through all the directories that match the wildcard format given below
for s in *_Guys
do
	cd $s #go into the sub directory

	sub=${PWD##*/} #get the subs dir name for the file name to be saved

	for f in "${Tracts[@]}"
	do 
		col="$(awk -F "	" '{ print $2}' $f)" #get the data in a row by row result for each fiber group
		echo $f
		echo $col >> "../${sub}_allData.txt" #stick the data in a text file.

	done
	
	cd ../ #bump back up a directory to the main one--a bit of a hack
done






