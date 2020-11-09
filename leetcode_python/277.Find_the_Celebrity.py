# https://leetcode.com/problems/find-the-celebrity/

# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:


class Solution:
    def findCelebrity(self, n: int) -> int:
        """
        0123456 7 89
                c
                
        01 -> know(0, 1) true: 0 is not c, 1 might be c
                        false: 1 is not c, 0 might be c
        """
        # first we need to find a candidate by looking through the list
        candidate = 0
        for i in range(1, n):
            if knows(candidate, i): # if candidate knows i, candidate must not be the celebrity while i might be the celebrity.
                candidate = i

        # after finding the candidate, we need to check if the candidate is valid.
        for i in range(n):
            if i != candidate and knows(candidate, i):   # check if candidate knows others. if yes, it is a invalid candidate
                return -1
            if not knows(i, candidate):   # check if all others know candidate. If not, it is a invalid candidate.
                return -1
        return candidate
