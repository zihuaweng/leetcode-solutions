# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/word-search-ii/


class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.word = None


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = self.build_trie(words)
        m = len(board)
        n = len(board[0])
        res = []
        for i in range(m):
            for j in range(n):
                self.dfs(board, i, j, root, res)
        return res

    def dfs(self, board, i, j, root, res):

        if root.word:  # find a word
            res.append(root.word)
            root.word = None  # avoid adding duplicated word

        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):   # Trie root is one behind the board[i][j], so we should add word first and check boundary.
            return

        c = board[i][j]
        p = root.children.get(c)
        if not p:
            return
        board[i][j] = '#'
        for _x, _y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            self.dfs(board, i + _x, j + _y, p, res)
        board[i][j] = c

    def build_trie(self, words):
        root = TrieNode()
        for w in words:
            p = root
            for char in w:
                p = p.children[char]
            p.word = w
        return root
