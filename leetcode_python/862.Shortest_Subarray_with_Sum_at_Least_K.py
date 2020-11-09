class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        """
        - similar to 239. Sliding Window Maximum
        - it contains negative numbers, so it could be any subsequence
        - xxxxx i[ xxx  j]  xx
        - for i < j, need to find pre_sum[j] - pre_sum[i] >= k
        - in order to get smaller j-i+1, i need to be the closest to j  
            -> if we get valid pre_sum[i], we need to keep looking for pre_sum[i+1]
            -> if pre_sum[j] < pre_sum[j-1], we don't need pre_sum[j-1] cause when j works as i, it will be more closer to the next j
            
            -> that means we need an pre_sum list that its index is increasing and its pre_sum is also increasing
            
        time O(n)
        space O(n)
        """
        
        q = collections.deque([(0, 0)])
        cur_sum = 0
        res = float('inf')
        
        for i, val in enumerate(A):
            cur_sum += val
            
            while q and cur_sum - q[0][1] >= K:
                res = min(res, i+1-q.popleft()[0])
            
            while q and cur_sum <= q[-1][1]:
                q.pop()
                
            q.append((i+1, cur_sum))
            
        if res != float('inf'):
            return res
        return -1