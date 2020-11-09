#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        c = collections.Counter(s)
        visited = collections.defaultdict(bool)
        stack = []
        for n in s:
            # print(c,visited)
            c[n] -= 1
            if not visited[n]:
                while stack and n <= stack[-1] and c[stack[-1]] != 0:
                    visited[stack.pop()] = False
                stack.append(n)
                visited[n] = True

        return ''.join(stack)


