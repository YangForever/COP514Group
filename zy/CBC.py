import numpy as np
import time
import encryption
import random
import decryption

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
    print '1'
    print mesg1
    print '2'
    print mesg2
    result = np.add(np.asarray(mesg1).astype(int), np.asarray(mesg2).astype(int)) % 2
    return result.astype(str)

def Encryp_Process(mesgBlocks):
    mesgFormer = IVec
    print 'IV'
    print IVec
    EnMesgBlocks = []
    for i in range(len(mesgBlocks)):
        print 'message'
        print mesgFormer
        mesg = mesgBlocks[i] # mesg ['1111111111(64)'] array
        en_input = BitewiseXOR(mesg, mesgFormer) # input ['1','0'(64)] array
        #print en_input
        en_input = [''.join(bit for bit in en_input)]
        #print en_input
        #print encryption.KEYS[0][0]
        first_xor = BitewiseXOR(en_input, encryption.KEYS[0])
        for j in range(5):
            print first_xor
            After_sub = encryption.Subsititution(first_xor) # After_sub 8x8 array
            After_per = encryption.Permutation(After_sub) # After_per 8x8 array
            en_input = encryption.BitewiseXOR(After_per, None, (j+1)).flatten()
        mesgFormer = [''.join(bit for bit in en_input)]
        EnMesgBlocks.append([''.join(bit for bit in mesgFormer)])
        print i
    return EnMesgBlocks
 
def Decryp_Process(hex_str):
    print 'Dectyp'
    EnMesgBlocks = GenDeBlocks(hex_str)
    reverse_Blocks = EnMesgBlocks[::-1]
    print reverse_Blocks
    b_num = len(reverse_Blocks)
    MesgBlocks = []
    for i in range(b_num):
        mesg = reverse_Blocks[i]
       # print mesg
        mesg = np.asarray(encryption.split_bits_string(mesg[0]))
       # print'mesg array'
       # print mesg
        for j in range(5):
            #print encryption.KEYS[i]
            After_XOR = decryption.de_BitewiseXOR(mesg, encryption.KEYS,(j+1))
            After_per = decryption.de_Permutation(After_XOR)
            mesg = decryption.de_Subsititution(After_per)
            #print j
        if (i+1) == b_num:
            mesgFormer = IVec
            print 'IV'
            print IVec
        else:
            mesgFormer = reverse_Blocks[i+1]
        mesg_flat = mesg.flatten()
        mesg = [''.join(bit for bit in mesg_flat)]
        print mesg
        print mesgFormer
        mesg = BitewiseXOR(mesg, encryption.KEYS[0])
        de_mesg = BitewiseXOR([mesg], mesgFormer)
        MesgBlocks.append([''.join(bit for bit in de_mesg)])
    return MesgBlocks

def GenDeBlocks(hex_str):
    bina_str = bin(int(hex_str, 16)).replace('0b', '')
    en_blocks = []
    i = 0
    while i < len(bina_str):
        en_blocks.append([bina_str[i:i+64]])
        i = i+64
    print en_blocks
    return en_blocks

def GenMesgBlocks(mesgString):
    b_mesg_string = ''.join([ '{0:07b}'.format(ord(c), 2) for c in mesgString])
    print b_mesg_string
    sLen = len(b_mesg_string)
    # print sLen
    mesgBlocks = []
    num1 = sLen/64
    j = 0
    if num1 > 0:
        for i in range(num1):
            mesgBlocks.append([b_mesg_string[j:(j + 64)]])
            j += 64
    extra_str = b_mesg_string[j:]
    #print type(extra_str)
    eLen = len(extra_str)
    zero_num = 64 - eLen
    zero_pad = ''.join('0' for i in range(zero_num))
    #print extra_str + zero_pad
    mesgBlocks.append([extra_str + zero_pad])
    return mesgBlocks    

def binaTostr(s):
    s_new = ''
    i = 0
    while i < len(s):
        if int(s[i:(i+7)], 2) == 0:
            break
        else:
            s_new += s[i:(i+7)]
            s_new += ' '
            i += 7
    return ''.join([chr(i) for i in [int(b, 2) for b in s_new[0:-1].split(' ')]])
            
#mesgBlocks = np.asarray([['1011001110110011101100110011010101010111101010111010101101010110'],
#    ['1011001110110011101100110011010101010111101010111010101101010110']])
def main_en(PlainText, IV, init_key):
    global IVec
    IVec = ['{0:064b}'.format(int(IV, 16))]
    encryption.Genkeys(init_key)
    mesgBlocks = GenMesgBlocks(PlainText)
    print mesgBlocks

    print 'PlainText:'
    for i in range(len(mesgBlocks)):
        print mesgBlocks[i]
    print '----------Encryption Process----------'
    msg = Encryp_Process(mesgBlocks)
    print '----------Cipher Text----------'
    Cipher = ''
    for i in range(len(msg)):
        Cipher += hex(int(msg[i][0], 2)).replace('0x', '').replace('L', '')
    print Cipher

def main_de(CipherText, IV, init_key):
    global IVec
    IVec = ['{0:064b}'.format(int(IV, 16))]
    encryption.Genkeys(init_key)
    mesgBlocks = CipherText
    print '----------Decryption Process----------'
    mesg = Decryp_Process(mesgBlocks)
    print '----------Plain Test----------'
    mesg = mesg[::-1]
    mesg = ''.join(item[0] for item in mesg)
    print binaTostr(mesg)



def encode(s):
    return ' '.join([bin(ord(c)).replace('0b', '') for c in s])

#print encode('hello world')

#print 'hh'

#print binaTostr('11010001100101110110011011001101111010000011101111101111111001011011001100100000000000000000000000000000000000000000000000000000')
#print binaTostr('11010001100101110110011011001101111')
main_en('hello world', '0101010101010101', '0101010101010101')
main_de('85c865156a63c6e73b1ef10d12376c1a', '0101010101010101', '0101010101010101')
