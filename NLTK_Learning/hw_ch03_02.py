#coding：utf-8
'''
算法思路：
将英文字按以下规则替换（除第一个字符外）：
   a e h i o u w y -> 0
   b f p v -> 1
   c g j k q s x z -> 2
   d t -> 3
   l -> 4
   m n -> 5
   r -> 6
去除0，对于重复的字符只保留一个
返回前4个字符，不足4位以0补足
'''
import re
def soundex(name):
    first = name[0]

    encoded = first.upper() + re.sub(r'[aehiouwy]', '', name[1:].lower())
    encoded = re.sub(r'[bfpv]', '1', encoded)
    encoded = re.sub(r'[cgjkqsxz]', '2', encoded)
    encoded = re.sub(r'[dt]', '3', encoded)
    encoded = re.sub(r'l', '4', encoded)
    encoded = re.sub(r'[mn]', '5', encoded)
    encoded = re.sub(r'r', '6', encoded)

    encoded_list = list(encoded)
    for i in range(1,len(encoded_list)):
        for j in range(i+1,len(encoded_list)):
            if (int(encoded_list[i] == encoded_list[j]) and int(encoded_list[i] != str(0)) ):
                encoded_list[j] = 0
    encoded = str(encoded_list).replace('\'','').replace('[','').replace(']','').replace(',','').replace(' ','')
    encoded = re.sub(r'0', '', encoded)
    if (len(encoded) < 4):
        encoded += '000'
    return encoded[:4]




print(soundex('Alan'))
print(soundex('Curry'))


