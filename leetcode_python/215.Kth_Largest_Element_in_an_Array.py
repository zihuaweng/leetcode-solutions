# https://leetcode.com/problems/kth-largest-element-in-an-array/
# https://github.com/Jack-Lee-Hiter/AlgorithmsByPython/blob/master/Target%20Offer/%E6%9C%80%E5%B0%8F%E7%9A%84k%E4%B8%AA%E6%95%B0.py
# 两个解答思路
# （1）快排序，找到最大的k个
# （2）最大堆算法，一直维护一个k大小的最大堆，里面最小的值就是需要的内容
# （3）priority tree ，root就是我们需要的结果（https://www.bilibili.com/video/av50936287?from=search&seid=8564690918367482337）

# 这里的最大堆最小堆算法
# Time complexity:  O(nlogn)
# Space complexity:  O(n)

# 这里的最大堆最小堆算法
# Time complexity:  O(k) + O((n-k) * logk)
# Space complexity:  O(K)

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        p = len(nums) - 1
        left = 0
        right = p
        while left < right:
            while left < right:
                while nums[left] < nums[p] and left < right:
                    left += 1
                while nums[right] >= nums[p] and left < right:
                    right -= 1
                if left != right:
                    nums[right], nums[left] = nums[left], nums[right]
            nums[right], nums[p] = nums[p], nums[right]
            if right == len(nums) - k:
                return nums[right]
            elif right > len(nums) - k:
                p = right - 1
                left = 0
                right = p
            else:
                left = right + 1
                right = p
        return nums[len(nums) - k]

    def findKthLargest2(self, nums: List[int], k: int) -> int:
        # 这里注意最大堆还会最小堆
        import heapq
        if len(nums) == 0 or k <= 0 or k > len(nums):
            return
        output = []
        for i in nums:
            if len(output) < k:
                output.append(i)
            else:
                output = heapq.nsmallest(k, output)
                if output[0] < i:
                    output[0] = i
        output = heapq.nsmallest(k, output)
        return output[0]

# 简单写法
    def findKthLargest(self, nums: List[int], k: int) -> int:

        #         [3,2,1,5,6,4]
        #          0  1
        #         [6  5]

        #         [3,2,3,1,2,4,5,5,6] and k = 4
        #         0 1 2 3
        #         [6 5 5 4]

        heap = []
        for n in nums:
            heapq.heappush(heap, n)
            if len(heap) > k:
                heapq.heappop(heap)
                
        return heapq.heappop(heap)