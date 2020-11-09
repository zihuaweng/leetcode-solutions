class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        """
        [3,1,2,4]

        - the result = A[i] * number of substring with min val equals to A[i]

        xxxx[xx i xxx]xx
           3 pos   4 pos
             num of substrings with min val equal to A[i] = 3*4
             sum of all substring with min val equal to A[i] = A[i] * (3*4)

        - how to find the range:
        xxxx[xx i xxx]xx
           |          |
         the first pre smaller or equal
                    the first next smaller

        223[5555 3 5555]22

        - how to get first pre smaller or equal
            3 55556 3   
            if pre > target, delete it, increasing stack
            importance: if there are same values, we only count the first smallest as the min

        - how to get first next smaller:
            3 55553 2   
            if pre > target, delete it, also increasing stack

        """
        n = len(A)
        first_pre = [-1] * n   # index of the first pre smaller or equal value
        first_next = [n] * n   # index of the first next smaller value
        
        stack = []
        for i, val in enumerate(A):
            while stack and A[stack[-1]] > val:
                stack.pop()
            if stack:
                first_pre[i] = stack[-1]
            stack.append(i)
            
        stack = []
        for i, val in enumerate(A):
            while stack and A[stack[-1]] > val:
                index = stack.pop()
                first_next[index] = i
            stack.append(i)
            
        res = 0
        for i in range(n):
            num_substring = (i-first_pre[i])*(first_next[i]-i)
            res += num_substring * A[i]
            res %= 10**9 + 7
            
        return res
                
                
        