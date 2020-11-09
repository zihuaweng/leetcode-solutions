# https://leetcode.com/problems/merge-intervals/
# 首先排序，遇到下一个的开始在上一个中间，替换一个终止

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
            
        intervals.sort()
        res = []
        start, end = intervals[0]
        for s, e in intervals[1:]:
            if s <= end:
                end = max(e, end)
            else:
                res.append([start, end])
                start = s
                end = e
        
        res.append([start, end])
                
        return res
        