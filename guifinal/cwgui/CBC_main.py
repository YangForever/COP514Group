import numpy as np
import time
import CBC_encryption as encryption
import random
import CBC_decryption as decryption
import OFB_write_file as write_file

IVec = []

'''def GenIVec():
    global IVec
    seed = random.randint(0, 9000000000000000000)
    iv = '{0:064b}'.format(seed)
    IVec.append(iv)
    IVec = np.asarray(IVec)  # IVec ['1111111111(64)'] array
'''
def BitewiseXOR(mesg1, mesg2): # mesg array
    mesg1 = encryption.split_bits_string(mesg1[0]) # need modify split_bits
    mesg2 = encryption.split_bits_string(mesg2[0])
    result = np.add(np.asarray(mesg1).astype(int), np.asarray(mesg2).astype(int)) % 2
    return result.astype(str)

def Encryp_Process(mesgBlocks):
    mesgFormer = IVec
    #print 'IV'
    #print IVec
    EnMesgBlocks = []
    for i in range(len(mesgBlocks)):
        #print 'message'
        #print mesgFormer
        mesg = mesgBlocks[i] # mesg ['1111111111(64)'] array
        en_input = BitewiseXOR(mesg, mesgFormer) # input ['1','0'(64)] array
        # #print en_input
        en_input = [''.join(bit for bit in en_input)]
        # #print en_input
        #print '00000'
        #print encryption.KEYS[0][0]
        en_input = BitewiseXOR(en_input, encryption.KEYS[0])
        for j in range(5):
            After_sub = encryption.Subsititution(en_input) # After_sub 8x8 array
            #print 'after_sub'
            #print After_sub
            After_per = encryption.Permutation(After_sub) # After_per 8x8 array
            #print 'after_per'
            #print After_per
            en_input = encryption.BitewiseXOR(After_per, None, (j+1)).flatten()
            #print 'after_xor'
            #print en_input

        mesgFormer = [''.join(bit for bit in en_input)]
        EnMesgBlocks.append([''.join(bit for bit in mesgFormer)])
        #print i
    return EnMesgBlocks
 
def Decryp_Process(hex_str):
    #print 'Dectyp'
    EnMesgBlocks = GenDeBlocks(hex_str)
    reverse_Blocks = EnMesgBlocks[::-1]
    #print 'reverse'
    #print reverse_Blocks
    b_num = len(reverse_Blocks)
    MesgBlocks = []
    for i in range(b_num):
        mesg = reverse_Blocks[i]
       # #print mesg
        mesg = np.asarray(encryption.split_bits_string(mesg[0]))
       # #print'mesg array'
       # #print mesg
        for j in range(5):
            # #print encryption.KEYS[i]
            After_XOR = decryption.de_BitewiseXOR(mesg, encryption.KEYS, j)
            #print 'xor'
            #print After_XOR
            After_per = decryption.de_Permutation(After_XOR)
            #print 'per'
            #print After_per
            mesg = decryption.de_Subsititution(After_per)
            #print 'sub'
            #print mesg
            # #print j
        if (i+1) == b_num:
            mesgFormer = IVec
            #print 'IV'
            #print IVec
        else:
            mesgFormer = reverse_Blocks[i+1]
        mesg_flat = mesg.flatten()
        mesg = [''.join(bit for bit in mesg_flat)]
        mesg = BitewiseXOR(mesg, encryption.KEYS[0])
        de_mesg = BitewiseXOR([mesg], mesgFormer)
        #print 'de_mesg'
        #print ''.join(bit for bit in de_mesg)
        MesgBlocks.append([''.join(bit for bit in de_mesg)])
    return MesgBlocks

def GenDeBlocks(hex_str):
    #print hex_str
    bina_str = ''.join([ '{0:04b}'.format(int(s, 16), 2) for s in hex_str])
    #print len(bina_str)
    en_blocks = []
    i = 0
    #print len(bina_str)
    while i < len(bina_str):
        en_blocks.append([bina_str[i:i+64]])
        i += 64
    #print en_blocks
    return en_blocks

def GenMesgBlocks(mesgString):
    b_mesg_string = ''.join([ '{0:08b}'.format(ord(c), 2) for c in mesgString])
    sLen = len(b_mesg_string)
    # #print sLen
    mesgBlocks = []
    num1 = sLen/64
    j = 0
    if num1 > 0:
        for i in range(num1):
            mesgBlocks.append([b_mesg_string[j:(j + 64)]])
            j += 64
    extra_str = b_mesg_string[j:]
    # #print type(extra_str)
    eLen = len(extra_str)
    zero_num = 64 - eLen
    zero_pad = ''.join('0' for i in range(zero_num))
    # #print extra_str + zero_pad
    mesgBlocks.append([extra_str + zero_pad])
    return mesgBlocks    

def binaTostr(s):
    s_new = ''
    # #print 'in'
    # #print s
    i = 0
    while i < len(s):
        if int(s[i:(i+8)], 2) == 0:
            break
        else:
            s_new += s[i:(i+8)]
            s_new += ' '
            i += 8
    # #print s_new
    return ''.join([chr(i) for i in [int(b, 2) for b in s_new[0:-1].split(' ')]])
            
#mesgBlocks = np.asarray([['1011001110110011101100110011010101010111101010111010101101010110'],
#    ['1011001110110011101100110011010101010111101010111010101101010110']])
def main_en(PlainText, IV, init_key):
    global IVec
    IVec = ['{0:064b}'.format(int(IV, 16))]
    encryption.Genkeys(init_key)
    mesgBlocks = GenMesgBlocks(PlainText)
    # #print mesgBlocks

    # #print 'PlainText:'
    # for i in range(len(mesgBlocks)):
    #     #print mesgBlocks[i]
    #     #print len(mesgBlocks[i][0])
    # #print '----------Encryption Process----------'
    msg = Encryp_Process(mesgBlocks)
    # #print '----------Cipher Text----------'
    Cipher = ''
    for i in range(len(msg)):
        # #print msg[i][0]
        Cipher += '{0:016X}'.format(int(msg[i][0], 2))
        # #print(Cipher)
    write_file.writeFile('test1.txt',Cipher)
    return Cipher

def main_de(CipherText, IV, init_key):
    global IVec
    IVec = ['{0:064b}'.format(int(IV, 16))]
    encryption.Genkeys(init_key)
    mesgBlocks = CipherText
    # #print '----------Decryption Process----------'
    mesg = Decryp_Process(mesgBlocks)
    # #print mesg
    # #print '----------Plain Test----------'
    mesg = mesg[::-1]
    mesg = ''.join(item[0] for item in mesg)
    # #print len(mesg)
    return binaTostr(mesg)



def encode(s):
    return ' '.join([bin(ord(c)).replace('0b', '') for c in s])

# #print encode('hello world')

# #print 'hh'

# #print binaTostr('11010001100101110110011011001101111010000011101111101111111001011011001100100000000000000000000000000000000000000000000000000000')
# #print binaTostr('11010001100101110110011011001101111')
#main_en('The BBC upsate jdkjaldkad djklajdkljnd mdakjldj? dajkdhkj. dajkghda, dakh?', '1234567890123445', '1234567890123456')
# main_de('9C39F823DE3FD7CD5467C3770273622F278455179F4C342F6AD59CAB24C7A2F0A991FBC607EDA2CF44D50E9DA29BCBBA09B2D98EF3FF73B91F56D7DEC137D375F6126736266511E4AE08FF14A52386A4', '1234567890123445', '1234567890123456')
