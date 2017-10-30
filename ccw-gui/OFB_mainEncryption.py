import OFB_encryption as encryption,OFB_changePCformat as changePCformat,OFB_hex2bin as hex2bin,OFB_xorOperation as xorOperation,OFB_encryptionProcess as encryptionProcess,OFB_checkPlaintext as checkPlaintext
def mainEncryption(plaintext,initialtext,cipherKey):

	plaintext = checkPlaintext.checkPlaintext(plaintext)
	rangek = len(plaintext)/16 
	b =[]
	for i in xrange(0,rangek):
		b.append(plaintext[i*16:i*16+16])

	encryptedText = []
	temp_initialText = initialtext
	for i in xrange(0,rangek):
		temp_initialText = encryptionProcess.encryProcess(temp_initialText,cipherKey)
		encryptedText.append(temp_initialText)

	matrix_e = []
	matrix_p = []
	for i in xrange(0,rangek):
		matrix_p.append(hex2bin.hex2bin(b[i]))
		matrix_e.append(hex2bin.hex2bin(encryptedText[i]))

	ciphertext_m = []
	ciphertext = []
	for i in xrange(0,rangek):
		ciphertext_m.append(xorOperation.xorOperation(matrix_e[i],matrix_p[i]))
		ciphertext.append(changePCformat.changePCformat(ciphertext_m[i]))

	return ciphertext