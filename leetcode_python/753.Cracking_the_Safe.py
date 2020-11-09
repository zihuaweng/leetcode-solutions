#!/usr/bin/env python3
# coding: utf-8

# https://leetcode.com/problems/cracking-the-safe/

# Time complexity: O()
# Space complexity: O()


class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        ans = '0' * (n-1)
        visited = set()
        for _ in range(k**n): # 因为有k**n种可能的组合，所以我们要走k**n遍
            for y in range(k-1, -1, -1):  # 搞不清楚为什么这里不能顺序走
                cur = ans[-n+1:] if n > 1 else ''
                temp = cur + str(y)
                if temp not in visited:
                    ans += str(y)
                    visited.add(temp)
                    break
        return ans


# set + dfs 后面的密码与前面的密码最后一个重复
# Time complexity: O()
# Space complexity: O()
class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        self.ans = '0' * n
        visited = set()
        visited.add(self.ans)
        self.total_num = k ** n
        self.dfs(visited, n, k)
        return self.ans

    def dfs(self, visited, n, k):
        if len(visited) == self.total_num:
            return True
        cur = self.ans[-n + 1:] if n > 1 else ""
        for y in range(k):
            new_str = cur + str(y)
            if new_str not in visited:
                visited.add(new_str)
                self.ans += str(y)
                if self.dfs(visited, n, k):
                    return True
                self.ans = self.ans[:-1]
                visited.remove(new_str)
        return False

