BInum = input("Enter a binary number: ")
strBInum = BInum[::-1]
HEX_num = ""


def hex_char(num):
    if 10 <= num and num <= 15:
        dic = {10:"A", 11:"B", 12:"C", 13:"D", 14:"E", 15:"F"}
        return dic[num]
    else:
        return str(num)
    return dic[num]


for i in range(0, len(strBInum), 4):
    nibble = strBInum[i: i+4]
    HEXdigit = 0
    for j in range(len(nibble)):
        HEXdigit += (int(nibble[j]))*(2**j)
    HEX_num += hex_char(HEXdigit)


print(HEX_num[::-1])
