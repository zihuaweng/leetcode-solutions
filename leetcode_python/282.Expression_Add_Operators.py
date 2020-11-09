#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O(4(n-1)) [所有数字中间有n-1个空格，每个空格可以有4种可能，+-*，或者没有东西，就是相连]
# Space complexity: O()

# https://leetcode.com/problems/expression-add-operators/


class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        """
        1 2 3
         +
         -
         *
         
        dfs + backtrack
        
        [12 + 3]     [- 4]  dfs(5568980898)
        pre_total     prev
        
        [12 + 3]     [- 4 * 5 * 56]  dfs(8980898)
        pre_total         prev
        
        """
        if not num:
            return []
        
        res = []
        self.dfs(num, 0, '', res, target, 0, 0)
        return res
    
    def dfs(self, num, idx, temp, res, target, prev_total, prev):
        if idx == len(num):
            if target == prev_total + prev:
                res.append(temp)
            return
        
        for i in range(idx+1, len(num)+1):
            if num[idx] == '0' and i > idx+1:   # 05 starts with 0 but isn't a valid number
                continue
                
            cur = num[idx:i]
            val = int(cur) 
            
            if idx == 0:    # we don't need to add operators to the first one
                self.dfs(num, i, cur, res, target, prev_total+prev, val)
            else:
                self.dfs(num, i, temp+'+'+cur, res, target, prev_total+prev, val)
                self.dfs(num, i, temp+'-'+cur, res, target, prev_total+prev, -val)
                self.dfs(num, i, temp+'*'+cur, res, target, prev_total, prev*val)
        
        