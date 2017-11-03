from numpy import *

def hex2dec(string_num):  
    return str(int(string_num.upper(), 16))

def padFormat(string_num):
    string_num = string_num[2:]
    str_length = 4 - len(string_num)
    pad_content = ''
    for x in xrange(str_length):
        pad_content += '0'
    return pad_content + string_num
    
def hex2bin(string):
    dec_num = []
    for x in xrange(0,16):
        dec_num.append(int(hex2dec(string[x])))
    bin_num = []
    for x in xrange(0,16):
        bin_num.append(padFormat(bin(dec_num[x])))

    matrix_num = ''
    for x in xrange(len(bin_num)):
        matrix_num += bin_num[x] 

    matrix_b = arange(64)
    matrix_b = matrix_b.reshape(8,8)

    for i in xrange(8):
        for j in xrange(8):
            matrix_b[i][j] = matrix_num[i*8+j]


    return matrix_b
 