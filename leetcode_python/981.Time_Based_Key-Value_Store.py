#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# 首先存进去map
# 然后使用二分搜索找到小于的值
class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        arr = self.d[key]
        l = 0
        r = len(arr)
        
        # using bisect.bisect_right()
        while l<r:
            mid = (l+r)//2
            if arr[mid][0] > timestamp:
                r = mid
            else:
                l = mid + 1
                
        if l==0:
            return ''
        return arr[l-1][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)