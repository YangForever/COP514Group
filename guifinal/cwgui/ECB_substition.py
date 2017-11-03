import ECB_s_box as s_box
def substition(text):
	result = ''
	for i in range(int(len(text)/2)):
		x = int(text[i*2],16)
		y = int(text[i*2+1],16)
		result += s_box.a[x][y]
	return result

def de_substition(text):
	result = ''
	for i in range(int(len(text)/2)):
		x = int(text[i*2],16)
		y = int(text[i*2+1],16)
		result += s_box.sboxInv[x][y]
	return result


