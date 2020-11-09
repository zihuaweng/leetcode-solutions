#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0
        n = len(secret)
        counter_s = collections.Counter(secret)
        counter_g = collections.Counter(guess)
        for i in range(n):
            if secret[i] == guess[i]:
                bulls += 1
                counter_g[guess[i]] -= 1
                counter_s[secret[i]] -= 1

        for key, val in counter_s.items():
            if key in counter_g:
                cows += min(val, counter_g[key])

        return "{}A{}B".format(bulls, cows)


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0
        n = len(secret)
        counter = collections.defaultdict(int)
        for i in range(n):
            s = secret[i]
            g = guess[i]
            if s == g:
                bulls += 1
            else:
                if counter[s] < 0: cows += 1
                if counter[g] > 0: cows += 1
                counter[s] += 1
                counter[g] -= 1

        return "{}A{}B".format(bulls, cows)




