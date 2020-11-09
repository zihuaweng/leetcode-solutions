#!/usr/bin/env python3
# coding: utf-8

# https://leetcode.com/problems/super-ugly-number/discuss/169815/Python-DP-solution-beats-93.7-extremely-detailed-explanation
#  使用dp方法做。
# Time complexity: O(nk)
# Space complexity: O(n)

class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        size = len(primes)
        # 这里面的index意思是dp里面存有的ugly数需要选择哪一个与对应的primer相乘
        # dp保存了所有前面的ugly数
        # ugly_num表示该个位置的primer应该相乘得到多少，最后选取一个最小的作为下一个ugly数
        ugly, dp, index, ugly_nums = 1, [1], [0] * size, [1] * size
        for i in range(1, n):
            # compute possibly ugly numbers and update index
            for j in range(0, size):
                if ugly_nums[j] == ugly:
                    ugly_nums[j] = dp[index[j]] * primes[j]
                    index[j] += 1
            # get the minimum
            ugly = min(ugly_nums)
            dp.append(ugly)
        return dp[-1]

    # 这里使用了heapq
    # https://leetcode.com/problems/super-ugly-number/discuss/76301/Python-generators-on-a-heap
    def nthSuperUglyNumber(self, n, primes):
        import heapq
        uglies = [1]
        def gen(prime):
            for ugly in uglies:
                yield ugly * prime
        merged = heapq.merge(*map(gen, primes))
        while len(uglies) < n:
            ugly = next(merged)
            if ugly != uglies[-1]:
                uglies.append(ugly)
        return uglies[-1]