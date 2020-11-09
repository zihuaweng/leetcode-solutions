# https://leetcode.com/problems/numbers-at-most-n-given-digit-set/

class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        """
        589858 len=5
        
        - for num at index 1 to 4, it could be any number and still smaller than n
        - we only need to create value with length 5 that is smaller
            - if the first num is smaller than the first num of n, the others could be any num
            - if the first num is equal to the first num of n, keep the same process to find valid.
        """
        count = 0
        l = len(str(n))
        l_d = len(digits)
        
        for i in range(1, l):
            count += l_d**i
            
        def dfs(idx, n):
            if idx == len(n):
                return 1
            
            count = 0
            
            for d in digits:
                num = int(d)
                if num < int(n[idx]):    # 第一个比较小的话后面可以是任意数
                    count += len(digits) ** (len(n)-idx-1)
                elif num == int(n[idx]):  # 第一个相同的需要继续递归
                    count += dfs(idx+1, n)
            return count
        
        return dfs(0, str(n)) + count