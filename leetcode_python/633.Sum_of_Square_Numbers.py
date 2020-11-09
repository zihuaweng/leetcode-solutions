class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        seen = set()
        for i in range(int(c**0.5)+1):
            seen.add(i*i)
            if c - i*i in seen:
                return True
        return False


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        """
        two sum in square value
        
        time O(sqrt(n))
        space O(1)
        """
        l = 0
        r = int(c**0.5)

        while l <= r:
            cur_sum = l**2 + r**2
            if cur_sum == c:
                return True
            elif cur_sum < c:
                l += 1
            else:
                r -= 1
                
        return False