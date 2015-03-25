import os, sys
from subprocess import Popen, PIPE

## Compiling input files
input_files = sys.argv[-1].split(',')

## Command skeleton
command = "Generate_trf.py ecmEnergy={0} "\
                           "maxEvents={1} "\
                           "runNumber={2} "\
                           "firstEvent={3} "\
                           "randomSeed={4} "\
                           "jobConfig={5} "\
                           "outputEVNTFile={6} "\
                           "inputGeneratorFile={7} "\
                           "evgenJobOpts={8}"

configurations = {
	'ee'     : (300001, 'jobConfig_ggZH_Ztoee.py',),
	'mumu'   : (300002, 'jobConfig_ggZH_Ztomumu.py',),
	'tautau' : (300003, 'jobConfig_ggZH_Ztotautau.py',)
}

for input_file in input_files:

	## configuration steering
	if   'ee'     in input_file: conf = configurations['ee']
	elif 'mumu'   in input_file: conf = configurations['mumu']
	elif 'tautau' in input_file: conf = configurations['tautau']
	else: conf = configurations['ee']

	runNumber = conf[0]
	jobConfig = conf[1]

	output_file_name = 'EVNT.root'

	formatted_command = command.format(8000,
	                                   28000,
	                                   runNumber,
					   5001,
	                                   43,
	                                   jobConfig,
	                                   output_file_name,
	                                   input_file,
	                                   'MC12JobOpts-00-09-52_v2.tar.gz'
	                                   )

	print '-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-'
	print 'Submitting ...'
	print formatted_command

	pout = Popen(args=formatted_command, stdout=PIPE, stderr=PIPE, shell=True).communicate()[0]

	f_out = open(output_file_name + 'log.out', 'w')
	f_out.write(pout)
	f_out.close()

	print 'Done with current submission.'

print 'All done.'
