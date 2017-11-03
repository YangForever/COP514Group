import numpy as np
import time
import CBC_s_box as s_box2
import random

def split_bits_string(mesg_string):
   # #print mesg_string
    mesg_bits = []
    for i in range(len(mesg_string)):
        mesg_bits.append(mesg_string[i])
    return mesg_bits

def de_Subsititution(mesg): # mesg array ['1','0','1','0'(64)]
   # #print sbox
    mesg.resize(8,8)   # [[],[]...] 8x8 array
    for i in range(len(mesg)):
        x = ''.join(bit for bit in mesg[i])
        hex_num = hex(int(x, 2))
        seq = int(hex_num, 0)
        # #print int(sbox[seq], 16)
        bit_string = '{0:08b}'.format(s_box2.sboxInv[seq])
        mesg[i] = split_bits_string(bit_string) # mesg should be [[],[]] 8x8 array
    return mesg

def de_Permutation(mesg): # mesg is 8x8 array
    row = len(mesg)
    col = len(mesg[0])
    # #print 'bits:'
    # #print mesg
    for i in range(0, col):
        j = 8-i
	mesg[:, i] = np.roll(mesg[:,i], j)
    return mesg
 
def de_BitewiseXOR(mesg, KEYS, turn_num): # mesg 8x8 array
    ##print KEYS
    #print 'mesg'
    #print mesg
    key = KEYS[-(1+turn_num)]
    #print 'key'
    #print key
    key = split_bits_string(key[0])
    Keyarray = np.asarray(key)
    result = np.add(Keyarray.flatten().astype(int), np.asarray(mesg).flatten().astype(int)) % 2
    #print 'reslut'
    #print result
    result = result.reshape(8,8)
    return result.astype(str)
