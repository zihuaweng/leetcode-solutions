class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        for x in nums1, find the same number in nums2 and check if there is any number larger than x (say the number is y>x) on its right side in nums2. Print y if there is such a number or -1 if there is no such number.
        
        if num2 =  [9, 8 ,7 , 6, 2 10]
        high(9) = 10
        high(8) = 10
        high(2) = 10
        so for a decreasing list, the high will return the first first big value, since we don't have duplicated value, we can use dict to store the high() result.
        """ 
        stack = []
        d = {}
        for num in nums2:
            while stack and stack[-1] < num:
                d[stack.pop()] = num
            stack.append(num)
            
        res = []
        for num in nums1:
            if num in d:
                res.append(d[num])
            else:
                res.append(-1)
        return res