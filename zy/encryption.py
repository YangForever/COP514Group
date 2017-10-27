import numpy as np
import time
import s_box

def split_bits(mesg):
    mesg_bits = []
    row_bits = []
    for i in range(mesg):
        for j in range(mesg[i]):
            row_bits.append(mesg[i][j])
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
    print mesg_bits
    for i in range(1, col)):
        for j in range(row):
            temp = mesg_bits[(j+i) % 8]
            mesg_bits[(j+i % 8)] = 
            
            
        


mesg = [['10111111'], ['01010101']]
mesg = Subsititution(mesg)
print mesg
