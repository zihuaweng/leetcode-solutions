class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        h   i   t
        25  25  25
        
        - bfs
        - change the word to a new word
            - keep track of all the word generated. (duplicated path)
        - search the word in the list  (transform the wordList to set)
            - found: path += 1, word - > new word, keep search new word
        - return when we find the first one
        
        """
        word_set = set(wordList)
        
        if endWord not in word_set:
            return 0
        
        queue = collections.deque([(beginWord, 1)])
        seen = set()
        seen.add(beginWord)
        
        while queue:
            word, steps = queue.popleft()
            if word == endWord:
                return steps
            for i in range(len(word)):
                for j in range(26):
                    char = chr(ord('a')+j)
                    new_word = word[:i] + char + word[i+1:]
                    if new_word not in seen and new_word in word_set:
                        queue.append((new_word, steps+1))
                        seen.add(new_word)
                        
        return 0