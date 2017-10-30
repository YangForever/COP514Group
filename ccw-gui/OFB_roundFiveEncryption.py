import OFB_substitution as substitution,OFB_hex2bin as hex2bin,OFB_xorOperation as xorOperation

def roundFiveEncryption(plaintext,cipherKey):

	afterSubstitution = substitution.substitutionModule(plaintext) #substitution
	# print a
	# print ''

	bin_plain = hex2bin.hex2bin(afterSubstitution) #transform into binary

	# print bin_plain

	key = hex2bin.hex2bin(cipherKey)
	# print key
	# print d
	# print ''
	afterXor = xorOperation.xorOperation(bin_plain,key) #xor
 	# print e
	# print ''

	return afterXor