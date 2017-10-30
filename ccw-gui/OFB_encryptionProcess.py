import OFB_encryption as encryption, OFB_changeKey as changeKey,OFB_changePCformat as changePCformat,OFB_roundFiveEncryption as roundFiveEncryption,OFB_hex2bin as hex2bin,OFB_xorOperation as xorOperation

def encryProcess(initialtext,cipherKey):

	matrix_i = hex2bin.hex2bin(initialtext)
	matrix_c = hex2bin.hex2bin(cipherKey)
	temp = xorOperation.xorOperation(matrix_i,matrix_c)
	initialtext = changePCformat.changePCformat(temp)
	key = hex2bin.hex2bin(cipherKey)
	cipherKey = changeKey.chang_key(key)
	cipherKey = changePCformat.changePCformat(cipherKey)

	i = 4
	while i>0:
		initialtext,cipherKey = encryption.encryptionProcess(initialtext,cipherKey)
# print plaintext1
# print cipherKey1
		initialtext = changePCformat.changePCformat(initialtext)
		cipherKey = changePCformat.changePCformat(cipherKey)
		i = i-1

	encryptedText = roundFiveEncryption.roundFiveEncryption(initialtext,cipherKey)
	encryptedText = changePCformat.changePCformat(encryptedText)
	# print encryptedText

	return encryptedText