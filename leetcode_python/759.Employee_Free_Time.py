# https://leetcode.com/problems/employee-free-time/

"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        arr = []
        for s in schedule:
            for data in s:
                arr.append(data)
                
        arr.sort(key=lambda x: x.start)
        
        res = []
        end = arr[0].end
        
        for s in arr[1:]:
            if s.start > end:
                new_s = Interval(end, s.start)
                res.append(new_s)
            end = max(end, s.end)
                
        return res        