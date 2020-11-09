import collections


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0
        counter = collections.Counter(secret)
        for i, val in enumerate(guess):
            if counter[val] != 0:
                if val == secret[i]:
                    bulls += 1
                else:
                    cows += 1
                counter[val] -= 1
        return "{}A{}B".format(bulls, cows)
