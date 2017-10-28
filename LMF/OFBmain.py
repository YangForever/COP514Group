import mainEncryption,readFile,write_file,asc2str


#load information
plaintext = readFile.readFile('test.txt',0)  #fourth question: read plaintext from file
length = len(plaintext)
print '\n'
  #fiveth question: padding the last block
initialtext = '0001020304050607'
cipherKey = '2b7e151628aed2a6'



#encryption
r_cipherText = mainEncryption.mainEncryption(plaintext,initialtext,cipherKey)   # first question and econd question and third question:encryption for several blocks
cipherText =''
for i in xrange(0,len(r_cipherText)):
	cipherText += r_cipherText[i]

cipherText_p = cipherText[0:length]

print 'cipherText:\n',cipherText_p,'\n'

write_file.writeFile('test1.txt',cipherText_p)



#decryption 
cipherText1 = readFile.readFile('test1.txt',1)
r_decryption = mainEncryption.mainEncryption(cipherText1,initialtext,cipherKey)	  # second question and third question: decryption for several blocks
r_decryptionT = ''
for i in xrange(0,len(r_decryption)):
	r_decryptionT += r_decryption[i]

r_decryptionT_p = r_decryptionT[0:length]

r_decryptionT_p = asc2str.asc2str(r_decryptionT_p)

print 'plaintext(processed):\n',r_decryptionT_p,'\n'