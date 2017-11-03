import OFB_s_box as s_box,OFB_hex2bin as hex2bin
def substitutionModule(string):
	sub_plaintext = string
	sBox = s_box.a
	changed_plaintext = ''
	for x in range(0,len(sub_plaintext)-1,2):
		i = int(hex2bin.hex2dec(sub_plaintext[x]))
		j = int(hex2bin.hex2dec(sub_plaintext[x+1]))
		changed_plaintext += sBox[i][j]
	return changed_plaintext

	