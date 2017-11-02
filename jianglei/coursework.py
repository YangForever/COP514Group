import numpy as np

def pseudo_random():
    s=[]
    s.append(5)
    a=20
    b=14
    for i in range(1,56):
        s.append((a*s[i-1]+b)%(2**31-1))
    newList=[x%2 for x in s]
    return newList

sbox= np.array(['63','7c','77','7b','f2','6b','6f','c5','30','01','67','2b','fe','d7','ab','76',
'ca','82','c9','7d','fa','59','47','f0','ad','d4','a2','af','9c','a4','72','c0',
'b7','fd','93','26','36','3f','f7','cc','34','a5','e5','f1','71','d8','31','15',
'04','c7','23','c3','18','96','05','9a','07','12','80','e2','eb','27','b2','75',
'09','83','2c','1a','1b','6e','5a','a0','52','3b','d6','b3','29','e3','2f','84',
'53','d1','00','ed','20','fc','b1','5b','6a','cb','be','39','4a','4c','58','cf',
'd0','ef','aa','fb','43','4d','33','85','45','f9','02','7f','50','3c','9f','a8',
'51','a3','40','8f','92','9d','38','f5','bc','b6','da','21','10','ff','f3','d2',
'cd','0c','13','ec','5f','97','44','17','c4','a7','7e','3d','64','5d','19','73',
'60','81','4f','dc','22','2a','90','88','46','ee','b8','14','de','5e','0b','db',
'e0','32','3a','0a','49','06','24','5c','c2','d3','ac','62','91','95','e4','79',
'e7','c8','37','6d','8d','d5','4e','a9','6c','56','f4','ea','65','7a','ae','08',
'ba','78','25','2e','1c','a6','b4','c6','e8','dd','74','1f','4b','bd','8b','8a',
'70','3e','b5','66','48','03','f6','0e','61','35','57','b9','86','c1','1d','9e',
'e1','f8','98','11','69','d9','8e','94','9b','1e','87','e9','ce','55','28','df',
'8c','a1','89','0d','bf','e6','42','68','41','99','2d','0f','b0','54','bb','16',])

def Substitution(inputval):
    # inputval include 8 characters. the shape of inputval is 1*8. i.e. inputval has 8 lists and every list has 8 elements.
    # so inputval has 64 elements in total.
    # the dimension of sbox has been changed as 1. therefore each character in the string can been transformed to the type of
    # int and find the corresponding value in sbox accorinding to the integer.
    block=np.reshape(inputval, [-1, 8])
    intlis = []
    for i in range(int(np.size(block)/8)):
        string = ''
        for b in block[i]:
            string+=str(b)
        intlis.append(sbox[int(string,2)])
    return intlis

# def hexTobinary(step1):
#     trans = [bin(int(t, 16)) for t in step1]
#     s = ''
#     for i in trans:
#         if len(i[2:]) < 8:
#             reverseString = i[::-1][0:len(i[2:])]
#             for j in range(8 - len(i[2:])):
#                 reverseString += '0'
#             s += reverseString[::-1]
#         else:
#             s += i[2:]
#     return s

def permutation(s):
    reverse=[]
    lst=np.reshape(list(s),[-1,8]).T
    reverse.append(lst[0])
    for iter in range(1,8):
        n=iter%8
        x = list(lst[iter][8-n::1])
        y = list(lst[iter][:8-n:1])
        reverse.append(x+y)
    return np.array(reverse).T

def Xor(reverse,K):
    result=np.zeros(np.shape(reverse),dtype=int)
    for i in range(np.size(reverse,0)):
        if np.size(reverse)==64:
            for j in range(np.size(reverse,1)):
                result[i][j]=int(reverse[i][j])^int(K[i][j])
        else:
            result[i] = int(reverse[i]) ^ int(K[i])
    return result

def readPlaintest(plaintext):
    batch=[]
    ASCcode=[bin(ord(text)+256)[3:] for text in plaintext]
    for i in range(int(len(ASCcode)/8)):
        batch.append(ASCcode[i*8:(i+1)*8])
    if len(ASCcode)%8==0:
        batchnumber=i+1
        paddingnumber=0
        return batch,batchnumber,paddingnumber
    else:
        paddingnumber=8 - len(ASCcode) % 8
        for j in range(paddingnumber):
            ASCcode.append('00000000')
        batch.append(ASCcode[len(ASCcode)-8:])
        batchnumber=i+2
        return batch,batchnumber,paddingnumber

def keyGenerator(key):
    key[0] = Xor(key[0],key[1])
    key[1] = list(bin(int('1' + Substitution(key[1])[0], 16))[3:])
    key[2] = Xor(key[2],key[3])
    key[3] = list(bin(int('1' + Substitution(key[3])[0], 16))[3:])
    key[4] = Xor(key[4],key[5])
    key[5] = list(bin(int('1' + Substitution(key[5])[0], 16))[3:])
    key[6] = Xor(key[6],key[7])
    key[7]= list(bin(int('1' + Substitution(key[7])[0], 16))[3:])
    return key

def encryption(inputval,key):
    for i in range(5):
        round1_step1 = Substitution(inputval)
        s = [bin(int('1' + t, 16))[3:] for t in round1_step1]
        reverse = permutation(''.join(s))
        inputval = Xor(reverse, key)
        key = keyGenerator(key)
    return inputval

def decryption(paddingnumber,batchnumber,outlis,cypher):
    plaintextRecover = []
    decrpt = ''
    for j in range(batchnumber):
      plaintextRecover.append(Xor(outlis[j], np.reshape(cypher[j], [8, 8])))
    plaintextRecoveroneDim = np.reshape(plaintextRecover, [-1, 8])
    for i in range((batchnumber) * 8-paddingnumber ):
        decrpt = decrpt + chr(int(''.join(str(s) for s in plaintextRecoveroneDim[i]), 2))
    print("decrption: ",decrpt)

#if __name__ == '__main__':
# plaintext='Bank statements will be reviewed to establish which funds belong to the paying parent, ' \
    #           'and both account holders will be given the right to make their case before any money is taken.'
    #plaintext='He added: "Speaking on behalf of the community our thoughts and prayers will all those ' \
         #     'affected. The community will come together and do all it can for the surviving children and relations."'

def main(count, plaintext, key):
    key_temp=''
    key_temp=key_temp+''.join([bin(int('1'+key1,16))[3:] for key1 in key])
    key=key_temp
    count_temp=''
    count_temp = count_temp + ''.join([bin(int('1' + count_initial, 16))[3:] for count_initial in count])
    count = np.reshape(list(count_temp), [8, 8])
    print("plaintext: ",plaintext)
    global paddingnumber,batchnumber1
    batch,batchnumber1,paddingnumber=readPlaintest(plaintext)
    cypher = []
    lis1 = [0, 0, 0, 0, 0, 0, 0, 1]
    for i in range(batchnumber1):
        inputval = count
        #key='1010100100100101111101011011010101010010001010100111101010101011'
        key=np.reshape(list(key),[-1,8])
        outputval=encryption(inputval, key)
        batch_plaintext=[]
        for col in range(8):
            batch_plaintext.append(np.reshape(list(batch[i][col]),[1,8]))
        cypher.append(Xor(outputval,np.reshape(batch_plaintext,[8,8])))
        text=''.join(str(e) for e in lis1)
        lis1=list(bin(int(text,2)+1+256)[3:])
        count[56:]=lis1
    shap=np.shape(cypher)
    output_t = np.reshape(cypher, [1, -1])[0]
    output_text = ''
    for i in range(0, int(len(output_t) / 4)):
        temp = output_t[i * 4:i * 4 + 4]
        b = hex(int(''.join(str(i) for i in temp), 2))
        output_text += b[2:]
    return output_text



def main1(count,cypher,key):
    cypher_temp = ''
    cypher_temp = cypher_temp + ''.join([bin(int('1' + cypher1, 16))[3:] for cypher1 in cypher])
    print (paddingnumber)
    cypher=np.reshape(np.array(list(cypher_temp)),[batchnumber1,8,8])
    key_temp = ''
    key_temp = key_temp + ''.join([bin(int('1' + key1, 16))[3:] for key1 in key])
    key = key_temp
    count_temp = ''
    count_temp = count_temp + ''.join([bin(int('1' + count_initial, 16))[3:] for count_initial in count])
    count = np.reshape(list(count_temp), [8, 8])
    batchnumber=len(cypher)
    batch=cypher
    lis1 = [0, 0, 0, 0, 0, 0, 0, 1]
    outlis = []
    cypher1=[]
    for i in range(batchnumber):
        inputval = count
        key = np.reshape(list(key), [-1, 8])
        outputval = encryption(inputval, key)
        outlis.append(outputval)
        a = []
        for col in range(8):
            a.append(np.reshape(list(batch[i][col]), [1, 8]))
        cypher1.append(Xor(outputval, np.reshape(a, [8, 8])))
        text = ''.join(str(e) for e in lis1)
        lis1 = list(bin(int(text, 2) + 1 + 256)[3:])
        count[56:] = lis1
    decryption(paddingnumber, batchnumber, outlis, cypher)
    return cypher1

cypher=main('1234567890123456','Bank statements will be reviewed to establish which funds belong to the paying parent, ' \
             'and both account holders will be given the right to make their case before any money is taken.', '0101010101010101')

print (cypher)

main1('1234567890123456',cypher,'0101010101010101')



