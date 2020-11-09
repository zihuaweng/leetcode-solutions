# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, arr: 'MountainArray') -> int:
        """
        1,2,3,[4],5,3,1
        
        1. find the peck, bs
        2. find target in the first half, bs
        3. find target in the second half, bs
        """
        # find the peck, using the same code as #852
        l = 0
        r = arr.length() - 1
        while l < r:
            mid = (l+r) // 2
            if arr.get(mid) < arr.get(mid+1):
                l = mid + 1
            else:
                r = mid
        
        peak = l
        
        # find the result in the first half
        l = 0
        r = peak
        while l <= r:
            mid = (l+r) // 2
            if arr.get(mid) == target:
                return mid
            elif arr.get(mid) < target:
                l = mid + 1
            else:
                r = mid - 1
        
        # find the result in the second half
        l = peak
        r = arr.length()-1
        while l <= r:
            mid = (l+r) // 2
            if arr.get(mid) == target:
                return mid
            elif arr.get(mid) > target:
                l = mid + 1
            else:
                r = mid - 1
                    
        return -1
        
        