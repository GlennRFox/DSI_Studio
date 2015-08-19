import subprocess #allows us to run the shell 
import glob #for dir searching
import sys

# #This script is meant to be run on one subject at a time. I do this so I can 
# see the results from each subject one at a time and make sure the data are okay. 
# #If you're picky, you can write your own loop to get through all your subs.


# Okay get started by loading the .fib file.  I only keep one in each sub dir, you can always
#change the wildcard statement or write another loop if you have more than one per sub
srcFiberFile=glob.glob('*.fib.gz') #use glob to get the .fib file in the dir
srcFiberFile = srcFiberFile[0]#set the first item to itself


# #WATCH OUT FOR________   W H I T E SPACE ___________    IN YOUR STRINGS!


#+++++++++++++++++++++++++++++++++++++++++++++++FIRST:

#++++++check the directory to make sure all the file names are compatible.

#These are all the ROIs used
fnames = [
'Callosum.nii.gz',
'Frontal_Pole.nii.gz', 
'Posterior_Block.nii.gz',
'Inferior_Block.nii.gz',
'MidSagittal.nii.gz',
'PostPole.nii.gz', 
'Inferior_Frontal.nii.gz',
'Superior_Frontal.nii.gz',
'L_Cingulum.nii.gz', 
'L_Temporal_Pole.nii.gz',
'L_External_Capsule.nii.gz', 
'L_Post-IFG.nii.gz',
'L_Pre-Wernicke.nii.gz',
'L_SFG-MFG.nii.gz', 
'L_Superior_Insula.nii.gz',
'L_Occipitoparietal.nii.gz',
'L_Thalamus.nii.gz',
'R_Cingulum.nii.gz', 
'R_Temporal_Pole.nii.gz',
'R_External_Capsule.nii.gz', 
'R_Post-IFG.nii.gz',
'R_Pre-Wernicke.nii.gz',
'R_SFG-MFG.nii.gz', 
'R_Superior_Insula.nii.gz',
'R_Occipitoparietal.nii.gz',
'R_Thalamus.nii.gz',
'Brainstem.nii.gz',
'MotorCortex.nii.gz',]

#check that they are all here
x = glob.glob('*.nii.gz')#get all the files in an array 
n = 0;
ex = 0;
for name in fnames:
	# print name
	if fnames[n] in x:
		print "" #print lots of space so it is easy to find the flawed files.
	else:
		print "Missing %s\n" % (name)
		ex = 1
	n+=1
#quit after we find missing files
if ex == 1:
	sys.exit('Fix missing files')


##+++++++++++++++++++++++++++++++++++++++++++SECOND:

#Set up your dictionary listing of your fiber groups and the ROIs they make
#This dictionary contains the code snippets that will go in the middle of the dsi-studio call as a string.  Keep the space after the single quote.
Tracts = {

'Callosum' : [' --roi Callosum.nii.gz --roa Inferior_Block.nii.gz'],
'Frontal_Pole' : [' --roi Frontal_Pole.nii.gz'],
'CallosalFrontal' : [' --roi Callosum.nii.gz --roi2 Frontal_Pole.nii.gz --roa Posterior_Block.nii.gz --roa2 Inferior_Block.nii.gz'],
'CallosalPosterior' : [' --roi Callosum.nii.gz --roi2 PostPole.nii.gz --roa Posterior_Block.nii.gz --roa2 Inferior_Block.nii.gz'],
'VerticalFrontal' : [' --roi Superior_Frontal.nii.gz --roi2 Inferior_Frontal.nii.gz'],
 'MotorTract' : [' --roi Brainstem.nii.gz --roi2 MotorCortex.nii.gz --roa Frontal_Pole.nii.gz --roa2 MidSagittal.nii.gz'],

'L_Cingulum' : [' --roi L_Cingulum.nii.gz --roa MidSagittal.nii.gz'],
'L_FrontoThalamic' : [' --roi L_Thalamus.nii.gz --roi2 Frontal_Pole.nii.gz --roa MidSagittal.nii.gz'],
'L_Uncinate_Fasciculus' : [' --roi L_Temporal_Pole.nii.gz --roi2 L_External_Capsule.nii.gz --roa Posterior_Block.nii.gz --roa2 MidSagittal.nii.gz --roa3 L_Superior_Insula.nii.gz'],
'L_IFOF' : [' --roi L_External_Capsule.nii.gz --roi2 PostPole.nii.gz --roi3 Frontal_Pole.nii.gz --roa MidSagittal.nii.gz --roa2 L_Temporal_Pole.nii.gz'],
'L_Arcuate' : [' --roi L_Post-IFG.nii.gz --roi2 L_Pre-Wernicke.nii.gz'],
'L_ShortAssociation' : [' --roi L_SFG-MFG.nii.gz --roa L_Superior_Insula.nii.gz --roa2 MidSagittal.nii.gz --roa3 L_Cingulum.nii.gz'],
'L_ILF' : [' --roi PostPole.nii.gz --roi2 L_Temporal_Pole.nii.gz --roa MidSagittal.nii.gz --roa2 L_External_Capsule.nii.gz --roa3 L_Thalamus.nii.gz --roa4 L_Occipitoparietal.nii.gz --roa5 Frontal_Pole.nii.gz'],

'R_Cingulum' : [' --roi R_Cingulum.nii.gz --roa MidSagittal.nii.gz'],
'R_FrontoThalamic' : [' --roi R_Thalamus.nii.gz --roi2 Frontal_Pole.nii.gz --roa MidSagittal.nii.gz'],
'R_Uncinate_Fasciculus' : [' --roi R_Temporal_Pole.nii.gz --roi2 R_External_Capsule.nii.gz --roa Posterior_Block.nii.gz --roa2 MidSagittal.nii.gz --roa3 R_Superior_Insula.nii.gz'],
'R_IFOF' : [' --roi R_External_Capsule.nii.gz --roi2 PostPole.nii.gz --roi3 Frontal_Pole.nii.gz --roa MidSagittal.nii.gz --roa2 R_Temporal_Pole.nii.gz'],
'R_Arcuate' : [' --roi R_Post-IFG.nii.gz --roi2 R_Pre-Wernicke.nii.gz'],
'R_ShortAssociation' : [' --roi R_SFG-MFG.nii.gz --roa R_Superior_Insula.nii.gz --roa2 MidSagittal.nii.gz --roa3 R_Cingulum.nii.gz'],
'R_ILF' : [' --roi PostPole.nii.gz --roi2 R_Temporal_Pole.nii.gz --roa MidSagittal.nii.gz --roa2 R_External_Capsule.nii.gz --roa3 R_Thalamus.nii.gz --roa4 R_Occipitoparietal.nii.gz --roa5 Frontal_Pole.nii.gz'],

} #end of tract dictionary

#Process the fiber tracts.
i = 0
for tract in Tracts:

	print tract

	#make the string to call to DSI_StudioCommands

	# #For the fiber tracking:
	TrackingCallInfo = "dsi_studio --action=trk --source=" + srcFiberFile + \
	" --method=1" + Tracts[tract][i] + \
	" --seed_count=50000 --step_size=.44 --turning_angle=70 --interpolation=0 \
	--fa_threshold=.15 --smoothing=0 --min_length=10 --max_length=300 \
	--output=" + tract + ".trk.txt"

	#call up dsiStudio through the shell using subprocess.Popen.  Careful with shell=True any code will run!!!
	subprocess.call(TrackingCallInfo, shell=True) #use subprocess.call allows it to wait for the thing to finish b4 returning

	#Run Statistics:
	StatCallInfo = "dsi_studio --action=ana --source=" + srcFiberFile + \
	" --tract=" + tract + ".trk.txt" + " --export=stat"
	#Call up dsiStudio
	subprocess.call(StatCallInfo, shell=True) 

	i += i
