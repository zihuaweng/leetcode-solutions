#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/open-the-lock/
# 注意先检查本身是不是deadlock

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        seen = set(deadends)
        queue = collections.deque(['0000'])
        res = 0
        while queue:
            length = len(queue)
            for _ in range(length):
                cur = queue.popleft()
                if cur == target:
                    return res
                if cur in seen:   # 有可能开始的地方已经是deadlock
                    continue
                seen.add(cur)
                for i in range(4):
                    cur_num = int(cur[i])
                    queue.append(cur[:i] + str((cur_num + 1) % 10) + cur[i + 1:])
                    queue.append(cur[:i] + str((cur_num - 1) % 10) + cur[i + 1:])
            res += 1
        return -1

