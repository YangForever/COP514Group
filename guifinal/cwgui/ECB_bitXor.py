def bitXor(stringA,stringB):
	stringA_p = ''
	for i in range(len(stringA)):
		temp = bin(int(stringA[i],16))[2:]
		stringA_p += temp.zfill(4)
	stringB_p = ''
	for i in range(len(stringB)):
		temp = bin(int(stringB[i],16))[2:]
		stringB_p += temp.zfill(4)
	result_l = ''
	for i in range(len(stringA_p)):
		result_l += str(int(stringA_p[i])^int(stringB_p[i]))
	output_s = ''
	for i in range(int(len(result_l)/4)):
		temp = str(hex(int(result_l[i*4:i*4+4],2)))[2:]
		output_s += temp
	return output_s


