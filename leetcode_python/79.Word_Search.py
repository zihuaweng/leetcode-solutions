# https://leetcode.com/problems/word-search/
# dfs思想，注意到了边界需要判断
# 记录走过没有可以直接替换原始board，这样可以节省空间
# 每次走完一步要记得回溯过去

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if word == '':
            return True
        m = len(board)
        if m == 0:
            return False
        n = len(board[0])
        if n == 0:
            return False
        # passed = [[False] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if self.helper(board, word, i, j):
                    return True

        return False

    def helper(self, board, word, row, col):
        if word == '':
            return True
        if col < 0 or col >= len(board[0]) or row < 0 or row >= len(board):
            return False
        if board[row][col] == '#' or board[row][col] != word[0]:
            return False

        temp = board[row][col]
        board[row][col] = '#'
        word = word[1:]

        if self.helper(board, word, row - 1, col) or self.helper(board, word, row + 1, col) or self.helper(board, word,
                                                                                                           row,
                                                                                                           col - 1) or self.helper(
                board, word, row, col + 1):
            return True
        # 要记得回溯
        board[row][col] = temp



class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        #         [
        #           ['A','B','C','E'],
        #           ['S','F','C','S'],
        #           ['A','D','E','E']
        #         ]

        #         visited =  [
        #           [False,'B','C','E'],
        #           ['S','F','C','S'],
        #           ['A','D','E','E']
        #         ]
        if not board:
            return False
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                if self.dfs(board, i, j, word):
                    return True
        return False

    def dfs(self, board, i, j, word):
        if not word:
            return True
        # 因为这里有判断，这个word是又前面的dfs生成的，对边界的判断应该放在最前面，如果没有判断word，例如计算island个数
        # 那样的可以放在生成了新的x,y后面立马判断。
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return
        if board[i][j] == "#" or board[i][j] != word[0]:
            return False
        temp = board[i][j]
        board[i][j] = "#"
        for x, y in [(i, j + 1), (i, j - 1), (i + 1, j), (i - 1, j)]:
            if self.dfs(board, x, y, word[1:]):
                return True
        board[i][j] = temp
        return False
