# https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/submissions/

# 第一种方法，使用trie来计算，
# 第一步：首先吧所有num转成一样长度的string（前面补充0），然后放到trie里面
# 第二步：每一个数我们从trie上往下找，尽量找一个当前位不同的数，返回该数与当前数的求xor
# https://youtu.be/wSgrc98d2lI

class Solution:
    def __init__(self):
        self.root = TrieNode()
    
    def insert_num(self, num):
        bits = bin(num)[2:].zfill(32)
        root = self.root
        for b in bits:
            root = root.children[b]
        
    def find_max(self, num):
        bits = bin(num)[2:].zfill(32)
        root = self.root
        max_val = ''
        for b in bits:
            target = '1' if b == '0' else '0'
            if target in root.children:
                max_val += target
                root = root.children[target]
            else:
                max_val += b
                root = root.children[b]
        return int(max_val, 2) ^ num
    
    def findMaximumXOR(self, nums: List[int]) -> int:
        # 第一步
        for num in nums:
            self.insert_num(num)
            
        # 第二步
        res = 0
        for num in nums:
            res = max(res, self.find_max(num))
            
        return res


# https://www.youtube.com/watch?v=ZHtZfkAcPKc
# 
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        res = 0
        for i in range(31, -1, -1):
            res <<= 1
            prev = {num >> i for num in nums}
            res += any(res^1^p in prev for p in prev)
            
        return res