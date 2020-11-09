class Solution:
    def balancedString(self, s: str) -> int:
        """
        We need to find the min string to replace, just use sliding window.
        Specilly this time we don't care the count of elements inside the window, we want to know the count outside the window.
        
        X X X X X X X
        O O[X X]O O O
        
        If [X X] is the part we need to replace, than the freq in [O O] [O O O] should be <= avg (len(s)//4)
        
        we first move the right pointer j to find a valid window, and then move left pointer i to right to get the min window 
        
        """
        i = 0
        res = float('inf')
        count = len(s) // 4
        d = collections.Counter(s)
        for j, val in enumerate(s):
            d[val] -= 1
            while i < len(s) and all(d[c] <= count for c in "QWER"):   # here we need to check i < len(s) in case of out of range error
                res = min(res, j-i+1)
                d[s[i]] += 1
                i += 1
            
        return res
        