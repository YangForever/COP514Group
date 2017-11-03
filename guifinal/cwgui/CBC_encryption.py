import numpy as np
import time
import CBC_s_box as s_box2
import random

KEYS = []

def split_bits_string(mesg_string):
   # #print mesg_string
    mesg_bits = []
    for i in range(len(mesg_string)):
        mesg_bits.append(mesg_string[i])
    return mesg_bits

def Subsititution(mesg): # mesg array ['1','0','1','0'(64)]
   # #print sbox
    mesg.resize(8,8)   # [[],[]...] 8x8 array
    for i in range(len(mesg)):
        x = ''.join(bit for bit in mesg[i])
        #print x
        hex_num = hex(int(x, 2))
        seq = int(hex_num, 0)
     #   #print str(s_box2.sbox[seq])
        bit_string = '{0:08b}'.format(s_box2.sbox[seq])
        mesg[i] = split_bits_string(bit_string) # mesg should be [[],[]] 8x8 array
    return mesg

def Permutation(mesg): # mesg is 8x8 array
    row = len(mesg)
    col = len(mesg[0])
    # #print 'bits:'
    # #print mesg
    for i in range(0, col):
	mesg[:, i] = np.roll(mesg[:,i], i)
    return mesg

def Genkeys(init_key): # 16 key
    global KEYS
    key_str = '{0:064b}'.format(int(init_key, 16))
    KEYS.append([key_str])
    for i in range(5):
        new_key = ''
        new_key += BitewiseXOR(key_str[0:8], key_str[8:16], 0)
        new_key += '{0:08b}'.format(s_box2.sbox[int(key_str[8:16],2)])

        new_key += BitewiseXOR(key_str[16:24], key_str[24:32], 0)
        new_key += '{0:08b}'.format(s_box2.sbox[int(key_str[24:32],2)])

        new_key += BitewiseXOR(key_str[32:40], key_str[40:48], 0)
        new_key += '{0:08b}'.format(s_box2.sbox[int(key_str[40:48],2)])

        new_key += BitewiseXOR(key_str[48:56], key_str[56:64], 0)
        new_key += '{0:08b}'.format(s_box2.sbox[int(key_str[56:64],2)])

        key_str = new_key
        KEYS.append([key_str])
    #print 'key'
    #for i in range(len(KEYS)):
        #print KEYS[i]

 
def BitewiseXOR(mesg1, mesg2 , round_num): # mesg 8x8 array
    if mesg2 == None:
        #print round_num
        key = split_bits_string(KEYS[round_num][0])
        Keyarray = np.asarray(key)
#       #print 'Key'
#       #print Keyarray[0]
#       #print 'flatten'
#       #print mesg.flatten()
        result = np.add(Keyarray.flatten().astype(int), mesg1.flatten().astype(int)) % 2
        return result.astype(str)
    #   #print result.astype(str)
    else:
        mesg1 = split_bits_string(mesg1)
        mesg2 = split_bits_string(mesg2)
        result = np.add(np.asarray(mesg1).flatten().astype(int), np.asarray(mesg2).flatten().astype(int)) % 2
        result = ''.join(str(bit) for bit in result)
        return result



