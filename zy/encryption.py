import numpy as np
import time
import s_box
import random

KEYS = []

def split_bits(mesg):
    print mesg
    mesg_bits = []
    for i in range(len(mesg)):
        row_bits = []
        for j in range(len(mesg[0][0])):
            row_bits.append(mesg[i][0][j])
        mesg_bits.append(row_bits)
    return mesg_bits

def Subsititution(mesg):
    sbox = s_box.a.flatten()
    print sbox
    for i in range(len(mesg)):
        hex_num = hex(int(mesg[i][0], 2))
        seq = int(hex_num, 0)
        print int(sbox[seq], 16)
        mesg[i][0] = '{0:08b}'.format(int(sbox[seq], 16))
    return mesg

def Permutation(mesg):
    mesg_bits = split_bits(mesg)
    row = len(mesg_bits)
    col = len(mesg_bits[0])
    print 'bits:'
    print mesg_bits
    mesg_bits = np.asarray(mesg_bits)
    for i in range(0, col):
	mesg_bits[:, i] = np.roll(mesg_bits[:,i], i)
    return mesg_bits

def Genkeys():
    global KEYS
    seed = random.randint(0, 30000)
    key = ['{0:016b}'.format(seed)]
    KEYS.append(key)   
 
def BitewiseXOR(mesg):
    keys = split_bits(KEYS)
    Keyarray = np.asarray(keys)
    #print 'Key'
    #print int(Keyarray[0])
    #print 'flatten'
    #print int(mesg.flatten())
    result = np.add(Keyarray[0].astype(int), mesg.flatten().astype(int)) % 2
    print result.astype(str)
    return result
            


mesg = [['10111111'], ['01010101']]
mesg = Subsititution(mesg)
mesg_bits = Permutation(mesg)
Genkeys()
result = BitewiseXOR(mesg_bits)

