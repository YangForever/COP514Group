import numpy as np
import time
import encryption
import random

IVec = []

def GenIVec():
    global IVec
    seed = random.randint(0, 9000000000000000000)
    iv = '{0:064b}'.format(seed)
    IVec.append(iv)
    IVec = np.asarray(IVec)  # IVec ['1111111111(64)'] array

def BitewiseXOR(mesg1, mesg2): # mesg array
    mesg1 = encryption.split_bits_string(mesg1[0]) # need modify split_bits
    mesg2 = encryption.split_bits_string(mesg2[0])
    result = np.add(np.asarray(mesg1).astype(int), np.array(mesg2).astype(int)) % 2
    return result.astype(str)

def Encryp_Process(mesgBlocks):
    GenIVec()
    mesgFormer = IVec
    EnMesgBlocks = []
    for i in range(len(mesgBlocks)):
        mesg = mesgBlocks[i] # mesg ['1111111111(64)'] array
        print mesg
        print IVec
        en_input = BitewiseXOR(mesg, mesgFormer) # input ['1','0'(64)] array
        for j in range(5):
            After_sub = encryption.Subsititution(en_input) # After_sub 8x8 array
            After_per = encryption.Permutation(After_sub) # After_per 8x8 array
            en_input = encryption.BitewiseXOR(After_per).flatten()

            time.sleep(10)
        mesgFormer = en_input
        EnMesgBlocks.append([''.join(bit for bit in mesgFormer)])
        print i
    return EnMesgBlocks

mesgBlocks = np.asarray([['1011001110110011101100110011010101010111101010111010101101010110']])
msg = Encryp_Process(mesgBlocks)
print msg
