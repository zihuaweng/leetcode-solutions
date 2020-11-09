class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        |____|  |____|   |____|   |____| 
               |_______________|
               
        1. add all intervals with end < new.start to the res, to ith interval
        2. new start = min(ith.start, new.start)
            while i+1.start <= new.end:
                end = max(ith.end, new.end)
                i += 1
                
        3. add the rest to res
        """
        n = len(intervals)
        i = 0
        res = []
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1
            
        if i == n:
            return res + [newInterval]
        
        new_start = min(intervals[i][0], newInterval[0])
        new_end = newInterval[1]
        
        while i < n and intervals[i][0] <= newInterval[1]:
            new_end = max(intervals[i][1], newInterval[1])
            i += 1
            
        res.append([new_start, new_end])
        
        while i < n:
            res.append(intervals[i])
            i += 1
            
        return res
        
        