import numpy as np
def permutatioin(text):
	text_t = ''
	for i in range(len(text)):
		temp = bin(int(text[i],16))[2:]
		text_t += temp.zfill(4)
	text_m = np.arange(64)

	for i in range(len(text_t)):
		text_m[i] = text_t[i]
	text_m = text_m.reshape(8,8)
	temp_matrix = np.arange(64)
	temp_matrix = temp_matrix.reshape(8,8)
	for i in range(0,8):
		for j in range(0,8):
			temp_matrix[(i+j)%len(text_m)][i] = text_m[j][i]

	temp_matrix = temp_matrix.reshape(1,64)[0]
	output_t = ''
	for i in range(int(len(temp_matrix)/4)):
		output_t += hex(int(''.join(temp_matrix[i*4:i*4+4].astype(str)),2))[2:]
	return output_t

def de_permutation(text):
	text_t = ''
	for i in range(len(text)):
		temp = bin(int(text[i],16))[2:]
		text_t += temp.zfill(4)
	text_m = np.arange(64)

	for i in range(len(text_t)):
		text_m[i] = text_t[i]
	text_m = text_m.reshape(8,8)
	temp_matrix = np.arange(64)
	temp_matrix = temp_matrix.reshape(8,8)
	for i in range(0,8):
		for j in range(0,8):
			temp_matrix[(j+len(text_m)-i)%len(text_m)][i] = text_m[j][i]
	temp_matrix = temp_matrix.reshape(1,64)[0]
	output_t = ''
	for i in range(int(len(temp_matrix)/4)):
		output_t += hex(int(''.join(temp_matrix[i*4:i*4+4].astype(str)),2))[2:]
	return output_t



