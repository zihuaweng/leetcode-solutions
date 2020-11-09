#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/find-the-duplicate-number/
# https://www.youtube.com/watch?v=dfIqLxAf-8s


# Solution 1 O(n)
# 遍历nums， 用value来当index查找，如果所对应的value是负数，证明当前index已经被查询过了，所以返回该index

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for n in nums:
            if nums[abs(n)] >= 0:
                nums[abs(n)] *= -1
            else:
                return abs(n)


# https://leetcode.com/problems/find-the-duplicate-number/discuss/72846/My-easy-understood-solution-with-O(n)-time-and-O(1)-space-without-modifying-the-array.-With-clear-explanation.
# Floyd's cycle-finding algorithm
# 这里一定会有一个环，所以可以设定一个fast，一个slow， fast走两步，slow走一步，到一个meeting  point后，fast变回0，从头开始一起走到一样的数字
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]         # 这里可以理解为，fast，和slow原来初始位置是0， 所以slow走了一步是nums[0]， fast走了两步是nums[nums[0]]
        fast = nums[nums[0]]
        while (slow != fast):
            slow = nums[slow]
            fast = nums[nums[fast]]

        fast = 0                # fast回到原始位置0
        while (fast != slow):
            fast = nums[fast]
            slow = nums[slow]

        return slow


# 同上，但是更好理解
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]
        match = False      # 下面相当于一个do{} while() loop， 如果直接判断while slow != fast， 那循环就不会开始，因为fast，slow初始值是一样的。
        while not match:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                match = True

        fast = nums[0]
        while (fast != slow):
            fast = nums[fast]
            slow = nums[slow]

        return slow