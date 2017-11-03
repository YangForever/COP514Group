import numpy as np, ECB_substition as substition
def changeKey(cipherkey):
	text_t = ''
	for i in range(len(cipherkey)):
		temp = bin(int(cipherkey[i],16))[2:]
		text_t += temp.zfill(4)
	text_m = np.arange(64)

	for i in range(len(text_t)):
		text_m[i] = text_t[i]
	text_m = text_m.reshape(8,8)
	temp_m = np.arange(64)
	temp_m = temp_m.reshape(8,8)
	temp = np.arange(8)
	for i in range(8):
		if i%2 == 0:
			for j in range(8):
				temp[j] = (text_m[i][j]+text_m[i+1][j])%2
			temp_m[i] = temp
		elif i%2 ==1 :
			text_str = ''.join(text_m[i].astype(str))
			t_str = ''
			t_str += hex(int(text_str[0:4],2))[2:]
			t_str += hex(int(text_str[4:8],2))[2:]
			f_str = substition.substition(t_str)
			str_t = ''
			for p in range(len(f_str)):
				temp_s = bin(int(f_str[p],16))[2:]
				str_t += temp_s.zfill(4)
			str_m = np.arange(8)
			for q in range(8):
				str_m[q] = str_t[q]
			temp_m[i] = str_m

	temp_m = temp_m.reshape(1,64)[0]
	output_t = ''
	for i in range(int(len(temp_m)/4)):
		output_t += hex(int(''.join(temp_m[i*4:i*4+4].astype(str)),2))[2:]
	return output_t


