class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        """
        [8,2,4,7]
        
        when we have a fixed left pointer i, we move right pointer j to the right to find the max valid window.
        then we can move the left pointer i to right to search for new window that start with i
        
        each time we need to calculate the limit:
            - max of the window   -> get it O(1) from max_queue, a monotone decreasing queue
            - min of the window   -> get it O(1) from min_queue, a monotone increasing queue
                
        """
        max_queue = collections.deque()
        min_queue = collections.deque()
        i = 0
        res = 0
        
        for j in range(len(nums)):
            while max_queue and nums[j] >= nums[max_queue[-1]]:
                max_queue.pop()
            max_queue.append(j)
            while min_queue and nums[j] <= nums[min_queue[-1]]:
                min_queue.pop()
            min_queue.append(j)
            
            while nums[max_queue[0]] - nums[min_queue[0]] > limit:
                i += 1
                while min_queue and i > min_queue[0]:
                    min_queue.popleft()
                while max_queue and i > max_queue[0]:
                    max_queue.popleft()
            res = max(res, j-i+1)
            
        return res