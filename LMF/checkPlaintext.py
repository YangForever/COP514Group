def checkPlaintext(plaintext):
	if(len(plaintext)%16 == 0):
		return plaintext
	else:
		num = len(plaintext)/16
		add_zero = (num+1) * 16 - len(plaintext)

		for i in xrange(0,add_zero):
			plaintext += '0'
	return plaintext


