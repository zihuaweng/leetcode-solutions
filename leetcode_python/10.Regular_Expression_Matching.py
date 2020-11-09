#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()


class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        "miss  iss  ippi"
        "mis*  is*   p*."

        "  aa  b"
        "c*a*  b"

        if not p:
            return not s

        first_match = len(s) > 0 and (p[0] == '.' or s[0] == p[0])

        if len(p) >= 2 and p[1] == '*':
            return self.isMatch(s, p[2:]) or (first_match and self.isMatch(s[1:], p))
        else:
            return first_match and self.isMatch(s[1:], p[1:])



# dp 方法
# https://www.youtube.com/results?search_query=10.+Regular+Expression+Matching
class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        # "  aa  b"
        # "c*a*  b"
        #       a  a b
        #   (T) F  F F
        # c F   F  F F
        # * (T) F  F F
        # a F   [T] F F
        # * (T) T [T] F
        # b F   F  F T

        m = len(p)
        n = len(s)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        # 第一个空字符串 对 空字符串 返回 true
        dp[0][0] = True
        # 第一列，隔一个是*的话就复制前一个的值
        for i in range(2, m + 1):
            if p[i - 1] == '*':
                dp[i][0] = dp[i - 2][0]

        for j in range(1, n + 1):
            for i in range(1, m + 1):
                if s[j - 1] == p[i - 1] or p[i - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[i - 1] == '*':
                    if p[i - 2] == s[j - 1] or p[i - 2] == '.':
                        dp[i][j] = dp[i - 2][j] or dp[i][j - 1]
                    else:
                        dp[i][j] = dp[i - 2][j]

        return dp[-1][-1]
