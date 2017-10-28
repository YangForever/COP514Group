import changeKey

def changePCformat(str_matrix):
	finalText = ''
	for i in xrange(0,len(str_matrix)):
		left = str_matrix[i][0:4]
		right = str_matrix[i][4:]
		left = changeKey.bin2hex(left)
		right = changeKey.bin2hex(right)
		finalText += hex(left)[2:]
		finalText += hex(right)[2:]
	return finalText

