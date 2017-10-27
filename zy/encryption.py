import numpy as np
import time
import s_box

def Subsititution(mesg):
    sbox = s_box.a.flatten()
    print sbox
    for i in range(len(mesg)):
        hex_num = hex(int(mesg[i][0], 2))
        seq = int(hex_num, 0)
        print int(sbox[seq], 16)
        mesg[i][0] = '{0:08b}'.format(int(sbox[seq], 16))
    return mesg


mesg = [['10111111'],['01010101']]
mesg = Subsititution(mesg)
print mesg
