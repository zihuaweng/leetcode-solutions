# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# 使用深度优先搜索算法。
# 递归进入最后一层然后每层都遍历


KEYBOARD = {
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z'],
}


class Solution:
    def letterCombinations(self, digits):
        res = []
        if not digits:
            return res

        self.dfs(digits, 0, '', res)
        return res

    def dfs(self, digits, index, string, res):
        if index == len(digits):
            res.append(string)
            return

        for i in KEYBOARD[digits[index]]:
            self.dfs(digits, index + 1, string + i, res)
