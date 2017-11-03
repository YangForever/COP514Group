import ECB_process as process,ECB_checktext as checktext,ECB_changeFormat as changeFormat,OFB_write_file as write_file

def Encryptionmain(plaintext,cipherkey):
	plaintext_a = ''
	for i in xrange(0,len(plaintext)):
		plaintext_a += str(ord(plaintext[i]))
	global length 
	length = len(plaintext_a)
	plaintext_t = checktext.checkPlaintext(plaintext_a)
	plaintext_arr = []
	for i in range(len(plaintext_t)/16):
		plaintext_arr.append(plaintext_t[i*16:i*16+16])
	output_str = ''
	for i in range(len(plaintext_t)/16):
		output_str += process.ecb_encryption(plaintext_arr[i],cipherkey)
	global leave
	leave = output_str[length:]
	write_file.writeFile('test1.txt',output_str[0:length])
	return output_str[0:length]

def Decryptionmain(ciphertext,cipherkey):
	ciphertext = ciphertext+leave
	num = len(ciphertext)/16
	ciphertext_arr = []
	for i in range(num):
		ciphertext_arr.append(ciphertext[i*16:i*16+16])
	output_cstr = ''
	for i in range(num):
		output_cstr += process.ecb_decryption(ciphertext_arr[i],cipherkey)
	output_cstr = changeFormat.asc2str(output_cstr[0:length])
	return output_cstr
