import OFB_encryption as encryption,OFB_changePCformat as changePCformat,OFB_roundFiveEncryption as roundFiveEncryption,OFB_hex2bin as hex2bin,OFB_xorOperation as xorOperation,OFB_encryptionProcess as encryptionProcess

plaintext = '4278b840fb44aaa7'
initialtext = '0001020304050607'
cipherKey = '2b7e151628aed2a6'

# #round1
# initialtext1,cipherKey1 = encryption.encryptionProcess(initialtext,cipherKey)
# # print plaintext1
# # print cipherKey1
# initialtext1 = changePCformat.changePCformat(initialtext1)
# cipherKey1 = changePCformat.changePCformat(cipherKey1)

# #round2
# initialtext2,cipherKey2 = encryption.encryptionProcess(initialtext1,cipherKey1)
# # print plaintext2
# # print cipherKey2
# initialtext2 = changePCformat.changePCformat(initialtext2)
# cipherKey2 = changePCformat.changePCformat(cipherKey2)

# #round3
# initialtext3,cipherKey3 = encryption.encryptionProcess(initialtext2,cipherKey2)
# # print plaintext2
# # print cipherKey2
# initialtext3 = changePCformat.changePCformat(initialtext3)
# cipherKey3 = changePCformat.changePCformat(cipherKey3)

# #round4
# initialtext4,cipherKey4 = encryption.encryptionProcess(initialtext3,cipherKey3)
# # print plaintext2
# # print cipherKey2
# initialtext4 = changePCformat.changePCformat(initialtext4)
# cipherKey4 = changePCformat.changePCformat(cipherKey4)

# #round5
# initialtext5 = roundFiveEncryption.roundFiveEncryption(initialtext4,cipherKey4)
# encryptedText = changePCformat.changePCformat(initialtext5)

#encryProcess
encryptedText = encryptionProcess.encryProcess(initialtext,cipherKey)
matrix_p = hex2bin.hex2bin(plaintext)
matrix_e = hex2bin.hex2bin(encryptedText)

#OFB Xor
ciphertext_m = xorOperation.xorOperation(matrix_e,matrix_p)
ciphertext = changePCformat.changePCformat(ciphertext_m)

#display
print 'plaintext:  ',plaintext
print 'cipherKey:  ',cipherKey
print 'initialtext:',initialtext
print 'ciphertext: ',ciphertext

#decryption
matrix_c = hex2bin.hex2bin(ciphertext)
a_plaintext_m = xorOperation.xorOperation(matrix_c,matrix_e)
a_plaintext = changePCformat.changePCformat(a_plaintext_m)
print 'decryption plaintext:',a_plaintext
