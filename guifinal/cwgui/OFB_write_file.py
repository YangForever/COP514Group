def writeFile(filename,ciphertext):
	output = open(filename,'w')
	output.write(ciphertext)
	output.close()
	print 'write to file \'test1\' finished\n'