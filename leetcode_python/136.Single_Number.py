# https://leetcode.com/problems/single-number/
# 第二种方法解释：
# Approach 4: Bit Manipulation
# Concept

# If we take XOR of zero and some bit, it will return that bit
# a \oplus 0 = aa⊕0=a
# If we take XOR of two same bits, it will return 0
# a \oplus a = 0a⊕a=0
# a \oplus b \oplus a = (a \oplus a) \oplus b = 0 \oplus b = ba⊕b⊕a=(a⊕a)⊕b=0⊕b=b
# So we can XOR all bits together to find the unique number.

class Solution:
    def singleNumber_1(self, nums) -> int:
        hash_table = {}
        for i in nums:
            try:
                hash_table.pop(i)
            except:
                hash_table[i] = 1
        return hash_table.popitem()[0]

    def singleNumber_2(self, nums):
        a = 0
        for i in nums:
            a ^= i
        return a
