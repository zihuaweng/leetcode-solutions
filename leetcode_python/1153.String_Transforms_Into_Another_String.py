#!/usr/bin/env python3
# coding: utf-8

# https://leetcode.com/problems/string-transforms-into-another-string/


# Time complexity: O(n)
# Space complexity: O()

# 因为每次转换，所有str1中所有相同的char都要转换
# 例如 ： ab -> ba
# 第一步： a转换成b，就有bb，第二个转换b -> 整个字符串会变成aa
# 所以，转换中出现有环，a->b->a
# 我们需要首先b->temp, a->b, temp->a
# 所以我们需要额外的一个char来做中间转换，如果所有26字母都用上了，就没有temp来完成转换
# 选择判断len(set(str2)) < 26是因为所有str1对str2可以多对一，所以len(set(str2)) <= len(set(str1))
class Solution:
    """
    str1 = "aabcc"
    str2 = "ccdee"
            "ccbcc"
            "ccdcc"
            "eedee"  (X)
    a -> c
    b -> d
    c -> e
    
    transformation of link link ,like a -> b -> c:
    we do the transformation from end to begin, that is b->c then a->b
    
    str1 = "aabcc"
    str2 = "ccdee"
            "aabee"
            "aadee"
            "ccdee"  
    c -> e
    b -> d
    a -> c
    

    str1 = "leetcode"
    str2 = "codeleet"

    l -> c
    e -> o
    e -> d? (X)

    brute force:
    1. as long as all same char in str1 match the same char in str2, they are able to transfer
    
    2. mapping stores all the mapping from str1 chars to str2 chars 
        d[l] = c , d[e] = o

    3. if d[char] != str2 coresponding char, return False

    corner case:
        1. len(str1) != len(str2): false
        2. there is a loop in the strings.  a->c , c->a.  
            a->temp, c->a, temp->c, we need an extrac char 
            str1 = "aabcc" 
            str2 = "ccdaa"
                    "aabaa"
                    "aadaa"
                    "ccdcc"  (X)
            
            len(set(str2)) != 26
        3. if str1 == str2: true
        

    time O(n)
    space O(n)
    """
    def canConvert(self, str1: str, str2: str) -> bool:
        if str1 == str2:
            return True
        d = {}
        for a, b in zip(str1, str2):
            if d.setdefault(a, b) != b:
                return False
        return len(set(str2)) < 26

