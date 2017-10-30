import OFB_mainEncryption as mainEncryption,OFB_readFile as readFile,OFB_write_file as write_file,OFB_asc2str as asc2str

def encryptionMain(plaintext,initialtext,cipherKey):
	plaintext_a = ''
	print 'plaintext:\n',plaintext
	for i in xrange(0,len(plaintext)):
		plaintext_a += str(ord(plaintext[i]))
	global length 
	length = len(plaintext_a)
	r_cipherText = mainEncryption.mainEncryption(plaintext_a,initialtext,cipherKey)
	cipherText =''
	for i in xrange(0,len(r_cipherText)):
		cipherText += r_cipherText[i]

	cipherText_p = cipherText[0:length]

	return cipherText_p

def decryptionMain(cipherText,initialtext,cipherKey):
	r_decryption = mainEncryption.mainEncryption(cipherText,initialtext,cipherKey)	  # second question and third question: decryption for several blocks
	r_decryptionT = ''
	for i in xrange(0,len(r_decryption)):
		r_decryptionT += r_decryption[i]

	r_decryptionT_p = r_decryptionT[0:length]
	print r_decryptionT_p

	r_decryptionT_p = asc2str.asc2str(r_decryptionT_p)

	return r_decryptionT_p