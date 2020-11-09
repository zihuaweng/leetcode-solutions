class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        """
        len = 6
        1 | 2 | 3 | 4 | 5 | 6
        
        find the max edges of each col
        1 2 2 1 =>
        1 | 23 | 45 | 6
        d[1] = 1
        d[3] = 1
        d[5] = 1
        
        3 1 2 =>
        123 | 4 | 56
        d[1] = 1
        d[3] = 2
        d[4] = 1
        d[5] = 1
        """
        d = collections.defaultdict(int)
        n = len(wall)
        
        for w in wall:
            pre_sum = 0
            for b in w[:-1]: # we don't need to add the last one
                pre_sum += b
                d[pre_sum] += 1
                
        if not d:
            return n
                
        return n - max(d.values())
        