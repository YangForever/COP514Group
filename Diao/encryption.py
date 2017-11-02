from numpy import *
import operator


a = array(
    [['63','7c','77','7b','f2','6b','6f','c5','30','01','67','2b','fe','d7','ab','76'],
     ['ca','82','c9','7d','fa','59','47','f0','ad','d4','a2','af','9c','a4','72','c0'],
     ['b7','fd','93','26','36','3f','f7','cc','34','a5','e5','f1','71','d8','31','15'],
     ['04','c7','23','c3','18','96','05','9a','07','12','80','e2','eb','27','b2','75'],
     ['09','83','2c','1a','1b','6e','5a','a0','52','3b','d6','b3','29','e3','2f','84'],
     ['53','d1','00','ed','20','fc','b1','5b','6a','cb','be','39','4a','4c','58','cf'],
     ['d0','ef','aa','fb','43','4d','33','85','45','f9','02','7f','50','3c','9f','a8'],
     ['51','a3','40','8f','92','9d','38','f5','bc','b6','da','21','10','ff','f3','d2'],
     ['cd','0c','13','ec','5f','97','44','17','c4','a7','7e','3d','64','5d','19','73'],
     ['60','81','4f','dc','22','2a','90','88','46','ee','b8','14','de','5e','0b','db'],
     ['e0','32','3a','0a','49','06','24','5c','c2','d3','ac','62','91','95','e4','79'],
     ['e7','c8','37','6d','8d','d5','4e','a9','6c','56','f4','ea','65','7a','ae','08'],
     ['ba','78','25','2e','1c','a6','b4','c6','e8','dd','74','1f','4b','bd','8b','8a'],
     ['70','3e','b5','66','48','03','f6','0e','61','35','57','b9','86','c1','1d','9e'],
     ['e1','f8','98','11','69','d9','8e','94','9b','1e','87','e9','ce','55','28','df'],
     ['8c','a1','89','0d','bf','e6','42','68','41','99','2d','0f','b0','54','bb','16']
     ]
)


def d_changeNum(len,list):
    for i in range(len):
        if list[i] == 'a':
            list[i] = 10
        elif list[i] == 'b':
            list[i] = 11
        elif list[i] == 'c':
            list[i] = 12
        elif list[i] == 'd':
            list[i] = 13
        elif list[i] == 'e':
            list[i] = 14
        elif list[i] == 'f':
            list[i] = 15


def d_ChangeToSBox(plainText):
    rowNum = 0
    colNum = 0
    temp = []
    for i in range(0,len(plainText),2):
        rowNum = int(plainText[i])
        colNum = int(plainText[i+1])
        temp.append(a[rowNum][colNum])
    return temp


def d_changeDataToBinary(hexadecimal):
    temp3 = []
    temp4 = []
    for i in range(len(hexadecimal)):
        a = bin(int(hexadecimal[i],16))
        b = a[2:]
        c = b.zfill(8)
        temp2 = []
        temp2.append(c)
        #print(temp2)
        temp3.append(temp2)

    for m in range(len(temp3)):
        str = ''.join(temp3[m])
        s = list(str)
        temp4.append(s)
    return temp4


def d_combin(plainText):
    temp = []
    for i in range(0,len(plainText),2):
        str = plainText[i] + plainText[i+1]
        temp.append(str)
    #print(temp)
    return temp


def d_DownWards(twoDimensionalArray):
    temp6 = []
    for i in range(len(twoDimensionalArray)):
        temp5 = [x[i] for x in twoDimensionalArray]
        #print(temp5)
        #print(i)
        num = len(twoDimensionalArray) - i
        temp5_1 = temp5[:num]
        temp5_1.reverse()
        #print(temp5_1)
        temp5_2 = temp5[num:]
        temp5_2.reverse()
        #print(temp5_2)
        temp5 = temp5_1 + temp5_2
        temp5.reverse()
        #print(temp5)
        temp6.append(temp5)
    #print(temp6)
    return temp6


def d_xOr(plaintext,plaintext1):
    temp = zeros(shape(plaintext))
    for i in range(len(plaintext)):
        for m in range(len(plaintext[i])):
            if plaintext[i][m] != plaintext1[i][m]:
                temp[i][m] = '1'
            else:
                temp[i][m] = '0'
    #print(temp)
    return temp


def d_getDifferentKeys(key):
    temp = zeros(shape(key))
    a = []
    c = []
    e = []
    for i in range(0,len(key),2):
        for j in range(len(key[i])):
            if key[i][j] != key[i+1][j]:
                temp[i][j] = 1
            else:
                temp[i][j] = 0
        temp1 = key[i + 1]
        #print(temp1)
        temp2 = temp1[0] + temp1[1] + temp1[2] + temp1[3] + temp1[4] + temp1[5] + temp1[6] + temp1[7]
        print(temp2)
        temp3 = hex(int(temp2, 2))
        temp4 = temp3[2:]
        temp5 = temp4.zfill(2)
        print(temp5)
        a.append(temp5)
    print(a)
    b = a[0]+a[1]+a[2]+a[3]
    for m in range(len(b)):
        str1 = ''.join(b[m])
        c.append(str1)
    #print(c)

    d_changeNum(len(c),c)
    #print(c)

    f = d_ChangeToSBox(c)

    g = d_changeDataToBinary(f)

    temp[1] = g[0]
    temp[3] = g[1]
    temp[5] = g[2]
    temp[7] = g[3]

    o = [[int(x) for x in inner] for inner in temp]
    e = [[str(x) for x in inner] for inner in o]

    return e

def d_ChangeIntToStr(temp):
    o = [[int(x) for x in inner] for inner in temp]
    e = [[str(x) for x in inner] for inner in o]
    #print(e)
    return e


def d_changeBack(plainText):
    a = []
    for i in range(len(plainText)):
        temp = plainText[i]
        temp1 = temp[0] + temp[1] + temp[2] + temp[3]
        temp4 = temp[4] + temp[5] + temp[6] + temp[7]
        temp2 = hex(int(temp1, 2))
        temp5 = hex(int(temp4, 2))
        temp3 = temp2[2:]
        temp6 = temp5[2:]
        a.append(temp3+temp6)

    #print(a)
    return a

def d_changeBackInt(plainText):
    a = []
    for i in range(len(plainText)):
        temp = plainText[i]
        temp1 = temp[0] + temp[1] + temp[2] + temp[3] + temp[4] + temp[5] + temp[6] + temp[7]

        temp2 = int(temp1, 2)
        #temp5 = int(temp4, 2)
        a.append(temp2)

    #print(a)
    return a

def d_splitStr(temp):
    temp1 = []
    for i in range(len(temp)):
        for x in temp[i]:
            temp1.append(x)
    #print(temp1)
    return temp1


def d_changeToAsc(temp):
    temp_back = []
    for i in range(len(temp)):
        temp1 = ord(temp[i])
        temp_back.append(temp1)
    #print(temp_back)
    return temp_back


def d_splitBlock(temp):
    a = len(temp)
    b = a // 8
    c = a%8
    d = []
    if b == 0:
        temp1 = zeros(8)
        temp1[:c] = temp
        for i in range(8-c):
            temp1[c+i] = 32
        return b+1,temp1
    else:
        temp3 = zeros(8-c)
        for m in range(8-c):
            temp3[m] = 32
        temp3 = list(temp3)
        #print(temp3)
        temp_result = temp + temp3
        #print(temp_result)
        for i in range(b+1):
            temp2 = zeros(8)
            d.append(temp_result[(i+1)*8-8:(i+1)*8])
        return b+1,d



def decrepte(ciphertext):
    list(ciphertext)
    num = len(cArr)
    finalList = list(zeros(num))
    print(num)
    dec_combine = d_combin(ciphertext)
    third = d_changeDataToBinary(dec_combine)
    print(third)
    #cArr[num-1] = d_ChangeIntToStr(cArr[num-1])
    third = d_ChangeIntToStr(third)
    d_cipher = d_xOr(third,cArr[num-2])
    h = d_changeBackInt(d_ChangeIntToStr(d_cipher))
    finalList[num-1] = h
    print(finalList)
    for i in range(num-2):
        cArr[num-i-2] = d_ChangeIntToStr(cArr[num-i-2])
        cArr[num-i-3] = d_ChangeIntToStr(cArr[num-i-3])
        #print(cArr[num-i-2])
        #print(cArr[num-i-3])
        #finalList[num-i-2] = d_xOr(cArr[num-i-2],cArr[num-i-3])
        finalList[num-i-2] = d_changeBackInt(d_ChangeIntToStr(d_xOr(cArr[num-i-2],cArr[num-i-3])))
    #print(finalList)
    finalList[0] = d_changeBackInt(d_ChangeIntToStr(d_xOr(cArr[0],result5)))
    finalList1 = []
    for m in range(len(finalList)):
        finalList1 = finalList1 + finalList[m]
    print(finalList1)
    temp1= []
    for j in range(len(finalList1)):
        temp0 = chr(int(finalList1[j]))
        temp1.append(temp0)
    print(temp1)
    diao = ''
    for k in range(len(temp1)):
        diao = str(diao)+temp1[k]
    return diao
















def main(plaintext,initialtext,cipherkey,flag):

    m = plaintext
    IV = initialtext
    d_key = cipherkey

    if(flag == 0):
        d_key_list = list(d_key)
        d_list = list(IV)

    #变成可以与Sbox相匹配的数值列表
        d_changeNum(len(d_list),d_list)
        #print(d_list)

    #与sBox相匹配找到对应值
        d_tempSbox = d_ChangeToSBox(d_list)
        #print(d_tempSbox)

    #print(d_tempSbox)
    #print(d_key_list)

    #将16个key值两两合并成8个
        d_key_list1 = d_combin(d_key_list)
        #print(d_key_list1)

    #将16个16进制的值转换为64个2进制的值
        d_tempBinary = d_changeDataToBinary(d_tempSbox)
        d_tempBinaryKey = d_changeDataToBinary(d_key_list1)
        #print(d_tempBinary)


    #根据算法，分别算出5个key值
        d_key1 = d_getDifferentKeys(d_tempBinaryKey)
        d_key2 = d_getDifferentKeys(d_key1)
        d_key3 = d_getDifferentKeys(d_key2)
        d_key4 = d_getDifferentKeys(d_key3)
    #print(d_key1)
    #print(d_key2)
    #print(d_key3)
    #print(d_key4)


    #先从8*8二维数组取出每一列元素组成新的8*8数组，再进行下降轮转，0列不动，7列移动7次
        d_down = d_DownWards(d_tempBinary)


    #形成的数组与key进行异或,得到第一轮结果
        result1 = d_xOr(d_down,d_tempBinaryKey)
        #print(result1)


    #将第一轮结果进行转成十六进制字符串列表，重新进行前面的操作
        strResult1 = d_ChangeIntToStr(result1)
        #print(strResult1)
        hexResult1 = d_changeBack(strResult1)
        #print(hexResult1)
        d_list1 = d_splitStr(hexResult1)


    #得到第二轮结果
        d_changeNum(len(d_list1), d_list1)
        d_down1 = d_DownWards(d_changeDataToBinary(d_ChangeToSBox(d_list1)))
        result2 = d_xOr(d_down1,d_key1)
        #print(result2)

    # 将第二轮结果进行转成十六进制字符串列表，重新进行前面的操作
        strResult2 = d_ChangeIntToStr(result2)
        hexResult2 = d_changeBack(strResult2)
        d_list2 = d_splitStr(hexResult2)

    # 得到第三轮结果
        d_changeNum(len(d_list2), d_list2)
        d_down2 = d_DownWards(d_changeDataToBinary(d_ChangeToSBox(d_list2)))
        result3 = d_xOr(d_down2, d_key2)
        #print(result3)

    # 将第三轮结果进行转成十六进制字符串列表，重新进行前面的操作
        strResult3 = d_ChangeIntToStr(result3)
        hexResult3 = d_changeBack(strResult3)
        d_list3 = d_splitStr(hexResult3)


    # 得到第四轮结果
        d_changeNum(len(d_list3), d_list3)
        d_down3 = d_DownWards(d_changeDataToBinary(d_ChangeToSBox(d_list3)))
        result4 = d_xOr(d_down3, d_key3)
        #print(result4)

    # 将第四轮结果进行转成十六进制字符串列表，重新进行前面的操作
        strResult4 = d_ChangeIntToStr(result4)
        hexResult4 = d_changeBack(strResult4)
        d_list4 = d_splitStr(hexResult4)


    # 得到第五轮结果
        d_changeNum(len(d_list4), d_list4)
        d_noPermutation = d_changeDataToBinary(d_ChangeToSBox(d_list4))
        global result5
        result5 = d_xOr(d_noPermutation, d_key4)
        #print(result5)


        d_block = d_changeToAsc(d_splitStr(m))
        d_time,d_block1 = d_splitBlock(d_block)
    #print(d_time)
        print(d_block1)

        m1 = d_block1[0]
        m_all = []
        for m in range(len(m1)):
            m_all.append(hex(int(m1[m])))
        m1_binary = d_changeDataToBinary(m_all)
    #print(m1_binary)
        result5 = d_ChangeIntToStr(result5)
        c1 = d_xOr(result5,m1_binary)
        print(c1)
        global cArr
        cArr = []
        cArr.append(c1)
    #print(cArr)

        for i in range(d_time-1):
            m2 = d_block1[i+1]
        #print(m2)
            m2_all = []
            for k in range(len(m2)):
                m2_all.append(hex(int(m2[k])))
        #print(m2_all)
            m2_binary = d_changeDataToBinary(m2_all)
        #print(m2_binary)
            cArr[i] = d_ChangeIntToStr(cArr[i])
            result6 = d_xOr(cArr[i],m2_binary)
            cArr.append(result6)

        final = cArr[d_time-1]
        print(final)
        final_Arr = d_changeBack(d_ChangeIntToStr(final))
        global temp
        temp = final_Arr[0]+final_Arr[1]+final_Arr[2]+final_Arr[3]+final_Arr[4]+final_Arr[5]+final_Arr[6]+final_Arr[7]
        print(temp)
        return temp
    else:
    #print(cArr)
        temp1 = decrepte(temp)
        return temp1

    # key = encryption(cArr[i])
    #  cArr.append(Xor(plaintext[i],key))






    #for i in range(d_time):
    #   temp_test = d_block1[i]
    #  temp_1 = []
    # for m in range(len(temp_test)):

    #    temp_1.append(hex(int(temp_test[m])))
#
#      d_mBinary = d_changeDataToBinary(temp_1)
#       c1 = d_xOr(result5,d_mBinary)


main('hello world','0987654321abcdfe','9876543210abdcfe',0)
main('7057939ab85e46c8','0987654321abcdfe','9876543210abdcfe',1)













