#!/usr/bin/env python3
# coding: utf-8

# https://leetcode.com/problems/optimal-account-balancing/

# Time complexity: O()
# Space complexity: O()


class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        """
        [[0,1,10], [1,0,1], [1,2,5], [2,0,5]]
        
        balance:
        0: -10 + 1 + 5 => -4
        1: 10 - 1 - 5 => 4
        2: 5 - 5 => 0
        
        0 + 1 == 0: balance
        
        [[0,1,10], [2,0,5]]
        
        0: -10 + 5 => -5
        1: 10 
        2: -5 
        
        1. calculate the balance of all nodes (dict)
        2. dfs backtrack to find the min path
        
            start: first n with debt
            end: reach the end of debt
            everytime pick the one with opposite sign 
            
        """
        total = collections.defaultdict(int)
        for s, r, money in transactions:
            total[s] -= money
            total[r] += money

        debt = [x for x in total.values() if x != 0]
        return self.dfs(debt, 0)

    def dfs(self, debt, idx):
        if idx == len(debt):
            return 0
        if debt[idx] == 0:
            return self.dfs(debt, idx + 1)

        trans = float('inf')
        for i in range(idx + 1, len(debt)):
            if debt[idx] * debt[i] < 0:
                debt[i] += debt[idx]
                trans = min(self.dfs(debt, idx + 1) + 1, trans)
                debt[i] -= debt[idx]

                # 加速运算，如果一次消清账单的话为最优
                if debt[idx] + debt[i] == 0:
                    break
        return trans