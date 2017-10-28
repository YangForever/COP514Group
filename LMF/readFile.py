import docx
def readFile(filename,flag):
	backNum = filename.find('.')
	if filename[backNum + 1:] == 'txt':
		file_obj = open(filename)
		try:
			all_text = file_obj.read()
		finally:
			file_obj.close()
	elif filename[backNum +1:] == 'docx' or filename[backNum +1:] == 'doc':
		try:
			file = docx.opendocx(filename)
			all_text = docx.getdocumenttext(file)[0].encode('raw_unicode_escape')	
		except Exception as e:
			raise IOError('file do not exist')
		finally:
			pass
		

	all_textAsc = ''
	if flag == 0:
		print 'plaintext:\n',all_text
		for i in xrange(0,len(all_text)):
			all_textAsc += str(ord(all_text[i]))
		return all_textAsc
	else:
		return all_text

