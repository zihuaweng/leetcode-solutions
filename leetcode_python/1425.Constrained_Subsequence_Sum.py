# https://leetcode.com/problems/constrained-subsequence-sum/

class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        """
        xxxxx[xxjxx] i
        - j - i <= k
        - we need to use dp, so for each j:
            - pick nums[j] and dp[i] , dp[j] = max(dp[i]....dp[j-1]) + nums[j]
                - we need to get the max of sliding window [i, j], an optimization is to use monotone decreasing queue O(k)
            - pick nums[j] as a new start  dp[j] = nums[j]
        
        since for each j we need to add nums[j], we can use nums as dp array
        """
        queue = collections.deque([])
        for j in range(len(nums)):
            if queue and j - queue[0] > k:
                queue.popleft()
            if queue:
                nums[j] = max(nums[j], nums[queue[0]]+nums[j])
            while queue and nums[queue[-1]] < nums[j]:
                queue.pop()
            queue.append(j)
        return max(nums)   # return the largest dp value