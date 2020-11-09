"""
1234 5
2226 3
    2

negative case:
34345
 -123       34345-123

    123
 -34345     -(34345-123) we can swith str1 and str2

 similar to 415 but need to process the data 
"""


def subtract(str1, str2):
    sign = 1
    final_sign = 1
    if str1[0] == '-' and str2[0] == '-':
        final_sign = -1
        str1 = str1[1:]
        str2 = str2[1:]
    elif str1[0] == '-':
        sign = -1
        str1 = str1[1:]
    elif str2[0] == '-':
        sign = -1
        str2 = str2[1:]
    
    if len(str1) < len(str2):
        str1, str2 = str2, str1
        if sign == -1:
            final_sign = -1

    i = len(str1) - 1
    j = len(str2) - 1
    res = ''
    carry = 0

    while i >= 0 or j >= 0:
        # print(i, j, carry)
        num = carry
        num += ord(str1[i]) - ord('0')
        if j >= 0:
            b = ord(str2[j]) - ord('0')
            num += b * sign

        res = str(num%10) + res
        carry = num//10
        i -= 1
        j -= 1

    if final_sign == -1:
        return '-' + res
    return res


print(subtract('123', '-234556'))  # -234433
print(subtract('123', '-234511'))  # -234388
print(subtract('234556', '-123'))  # 234433
print(subtract('234556', '123'))  # 234679
print(subtract('-123', '-234556'))  # -234679

