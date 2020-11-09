#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/sliding-puzzle/

class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        nums = ''.join(str(a) for b in board for a in b)
            
        index = nums.index('0')
        target = '123450'
        seen = set()
        
        queue = collections.deque([(index, nums)])
        res = 0
        while queue:
            for _ in range(len(queue)):
                i, n = queue.popleft()
                seen.add((i,n))
                if n == target:
                    return res
                x = i // 3
                y = i % 3
                for new_x, new_y in [(x, y+1), (x, y-1), (x-1, y), (x+1, y)]:
                    if 0 <= new_x < 2 and 0<= new_y < 3:
                        new_i = 3*new_x + new_y
                        temp = list(n)
                        temp[i], temp[new_i] = temp[new_i], temp[i]
                        new_n = ''.join(temp)
                        if (new_i, new_n) not in seen:
                            queue.append((new_i, new_n))
                            
            res += 1
        return -1
                
                
                