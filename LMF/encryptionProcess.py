import encryption,changePCformat,roundFiveEncryption,hex2bin,xorOperation

def encryProcess(initialtext,cipherKey):
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