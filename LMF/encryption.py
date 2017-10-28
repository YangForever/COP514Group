import substitution,hex2bin,shift_column,xorOperation,changeKey

def encryptionProcess(plaintext,cipherKey):

	afterSubstitution = substitution.substitutionModule(plaintext) #substitution
	# print a
	# print ''

	bin_plain = hex2bin.hex2bin(afterSubstitution) #transform into binary
	# print b
	# print ''
	afterPermutation = shift_column.shift_column(bin_plain) #permutation
	# print c
	# print ''

	key = hex2bin.hex2bin(cipherKey)
	# print d
	# print ''
	afterXor = xorOperation.xorOperation(afterPermutation,key) #xor
 	# print e
	# print ''

	afterChange_key = changeKey.chang_key(key) #change key

	return afterXor,afterChange_key