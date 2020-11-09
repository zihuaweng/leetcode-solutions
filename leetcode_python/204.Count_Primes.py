#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/count-primes/
# https://en.wikipedia.org/wiki/Sieve_of_Eratosthene
# 质数

class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        primes = [True] * n
        primes[0] = primes[1] = False
        # Use upper limit of (n**0.5)+1, because:
        #  (a) the smallest factor of a non-prime number will not be > sqrt(n).
        #      Ex. non-prime = 100,
        #           5*20
        #           10*10,
        #           20*5   # !! we have seen 5 before.
        for i in range(int(n**0.5)+1):
            if primes[i]:
                for j in range(i+i, n, i):
                    primes[j] = False
        return sum(primes)