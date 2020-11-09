class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        res = []
        word_set = set(words)
        seen = {}
        
        def dfs(word):
            if word in seen:
                return seen[word]
            
            for i in range(1, len(word)):
                if word[:i] in word_set:
                    suffix = word[i:]
                    if suffix in word_set or dfs(suffix):
                        seen[word] = True
                        return True
                        
            seen[word] = False
            return False
        
        
        for word in words:
            if dfs(word): 
                res.append(word)
                
        return res