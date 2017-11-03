import ECB_permutation as permutatioin,ECB_bitXor as bitXor,ECB_substition as substition,ECB_changekey as changeKey

def ecb_encryption(plainText,cipherKey):
	cipherKey_a = []
	cipherKey_a.append(cipherKey)
	for k in range(5):
		cipherKey_a.append(changeKey.changeKey(cipherKey_a[k]))
	processedText1 = bitXor.bitXor(plainText,cipherKey_a[0])
	i = 4
	while(i):
		processedText2 = substition.substition(processedText1)
		processedText3 = permutatioin.permutatioin(processedText2)
		processedText4 = bitXor.bitXor(processedText3,cipherKey_a[5-i])
		i = i-1
		processedText1 = processedText4

	resultedText_i = substition.substition(processedText1)
	resultedText_f = bitXor.bitXor(resultedText_i,cipherKey_a[5])
	return resultedText_f


def ecb_decryption(cipherText,cipherKey):
	cipherKey_b = []
	cipherKey_b.append(cipherKey)
	for k in range(5):
		cipherKey_b.append(changeKey.changeKey(cipherKey_b[k]))
	deprocessedText1 = bitXor.bitXor(cipherText,cipherKey_b[5])
	deprocessedText2 = substition.de_substition(deprocessedText1)
	i = 4
	while(i):
		deprocessedText3 = bitXor.bitXor(deprocessedText2,cipherKey_b[i])
		deprocessedText4 = permutatioin.de_permutation(deprocessedText3)
		deprocessedText2 = substition.de_substition(deprocessedText4)
		i = i-1
	deprocessedText5 = bitXor.bitXor(deprocessedText2,cipherKey_b[0])
	resultText = deprocessedText5
	return resultText
