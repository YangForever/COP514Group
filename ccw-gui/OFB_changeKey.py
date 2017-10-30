import OFB_s_box as s_box,OFB_hex2bin as hex2bin
import OFB_xorOperation as xorO

def bin2dec(string_num):
    return str(int(string_num, 2))

def bin2hex(byte_num):
	one = pow(2,0)
	two = pow(2,1)
	three = pow(2,2)
	four = pow(2,3)
	totalNum = int(byte_num[0])*four + int(byte_num[1])*three + int(byte_num[2])*two + int(byte_num[3])*one
	return totalNum




def chang_key(cipherKey):
	# print cipherKey
	box_s = s_box.a
	for i in xrange(0,len(cipherKey)):
		if(i%2==0):
			temp_cipher = ''
			for j in xrange(0,len(cipherKey[i])):
				temp_cipher += str(xorO.mod_operation(cipherKey[i][j],cipherKey[i+1][j]))
			for j in xrange(0,len(temp_cipher)):
				cipherKey[i][j] = temp_cipher[j]
		elif(i%2!=0):
			left = cipherKey[i][0:4]
			right = cipherKey[i][4:]
			left = bin2hex(left)
			right = bin2hex(right)
			temp_cipher = s_box.a[left][right]
			# print temp_cipher
			left = hex2bin.padFormat(bin(int(hex2bin.hex2dec(temp_cipher[0]))))
			right = hex2bin.padFormat(bin(int(hex2bin.hex2dec(temp_cipher[1]))))
			temp_cipher = left + right
			for j in xrange(0,len(temp_cipher)):
				cipherKey[i][j] = temp_cipher[j]
	return cipherKey



