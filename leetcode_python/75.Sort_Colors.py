# https://leetcode.com/problems/sort-colors/
# 第一种方法比较简明，走两次，第一次判断0的左移，第二次1左移，剩下的就是2了。


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        head = 0
        for i in range(2):
            for j in range(head, len(nums)):
                if nums[j] == i:
                    nums[head], nums[j] = nums[j], nums[head]
                    head += 1


# 第二种方法只走一次
# 一个指针在前，确定01分界，一个在后，确定12分界
# p指针一直往后走，判断值并移动

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        head = 0
        p = 0
        end = len(nums) - 1
        while p <= end:
            if nums[p] == 0:
                nums[p], nums[head] = nums[head], nums[p]
                p += 1
                head += 1
            elif nums[p] == 1:
                p += 1
            else:
                nums[p], nums[end] = nums[end], nums[p]
                end -= 1
                # 这里最后不用p+=1,因为移动了2有可能得到一个值是0，这样需要再一步调整。