# https://leetcode.com/problems/climbing-stairs/
# 这个上楼每次只能走两步或者一步，意味着，只能从前面一个走一步到，或者前面第二个走两步到，所以到达的可能数
# 就是到达前面一个+到达前面第二个的数量之和。
# 所以就是典型的斐波那契数列变换，f(n) = f(n-1) + f(n-2)


class Solution:
    def climbStairs(self, n: int) -> int:
        paths = [1, 2]
        if n < 3:
            return paths[n - 1]
        for i in range(2, n):
            index = i % 2
            paths[index] = paths[0] + paths[1]

        return max(paths)
