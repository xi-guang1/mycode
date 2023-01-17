import numpy as np

def Encryption(s:str):
    
    s = ''.join(format(ord(x), '08b') for x in s)
    s1 = s[::2]
    s2 = s[1::2]
    lst = [s1[i]+s2[i] for i in range(len(s) // 2)]
    res = '啊'
    for i in lst:
        if i == '00':
            res += '啊'
        elif i == '01':
            res += '呜'
        elif i == '10':
            res += '嗷'
        else:
            res += '~'
    print(len(s))
    return res
    
    
def Decryption(s:str):
    if s[0] != '啊':
        return '似乎不是一个有效的密文'
    s = s[1::]
    res = '08b'
    for i in s:
        if i == '啊':
            res += '00'
        elif i == '呜':
            res += '01'
        elif i == '嗷':
            res += '10'
        elif i == '~':
            res += '11'
        else:
            return '似乎不是一个有效的密文'
    print(res)
    print(chr(int(res,1)))
    

Decryption(Encryption('我是二臂'))
# print(bin('为啥'))
