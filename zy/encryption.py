import numpy as np
import time
import s_box
import random

KEYS = []

def split_bits_string(mesg_string):
   # print mesg_string
    mesg_bits = []
    for i in range(len(mesg_string)):
        mesg_bits.append(mesg_string[i])
    return mesg_bits

def Subsititution(mesg): # mesg array ['1','0','1','0'(64)]
    sbox = s_box.a.flatten()
   # print sbox
    mesg.resize(8,8)   # [[],[]...] 8x8 array
    for i in range(len(mesg)):
        x = ''.join(bit for bit in mesg[i])
        hex_num = hex(int(x, 2))
        seq = int(hex_num, 0)
    #    print int(sbox[seq], 16)
        bit_string = '{0:08b}'.format(int(sbox[seq], 16))
        mesg[i] = split_bits_string(bit_string) # mesg should be [[],[]] 8x8 array
    return mesg

def Permutation(mesg): # mesg is 8x8 array
    row = len(mesg)
    col = len(mesg[0])
    print 'bits:'
    print mesg
    for i in range(0, col):
	mesg[:, i] = np.roll(mesg[:,i], i)
    return mesg

def Genkeys():
    global KEYS
    seed = random.randint(0, 30000)
    key = ['{0:016b}'.format(seed)]
    KEYS.append(key)
    return key
 
def BitewiseXOR(mesg): # mesg 8x8 array
    key = Genkeys()
    Keyarray = np.asarray(key)
    #print 'Key'
    #print int(Keyarray[0])
    #print 'flatten'
    #print int(mesg.flatten())
    result = np.add(Keyarray[0].astype(int), mesg.flatten().astype(int)) % 2
    #print result.astype(str)
    return result.astype(str)
