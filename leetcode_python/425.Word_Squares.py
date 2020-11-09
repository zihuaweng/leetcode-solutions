# https://leetcode.com/problems/word-squares/

class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        """
        dfs + backtrack
        
        first pick a word, fill the row and col
        b a l l
        a
        l
        l
        
        and then pick the other work starts with a, (optimization: use dict to store the prefix, otherwise, TLE)
        b a l l
        a r e a
        l e 
        l a
        
        b a l l    row = 0
        a r e a    row = 1
        l e        row = 2
        l a        row = 3
        
        if we can't fill all the cells, backtrack
        """
        if not words:
            return []
        
        n = len(words[0])
        res = []
        d = self.get_prefix(words)
        
        self.dfs(words, n, 0, d, [], res) # todo
        return res
    
    
    def dfs(self, words, n, row, d, temp, res):
        if n == row:
            res.append(temp)
            return
        
        prefix = ''
        for i in range(row):
            prefix += temp[i][row]
            
        for w in d[prefix]:
            self.dfs(words, n, row+1, d, temp+[w], res)
        
    def get_prefix(self, words):
        d = collections.defaultdict(list)
        n = len(words[0])
        for w in words:
            for i in range(n+1):
                d[w[:i]].append(w)
        return d
        
        