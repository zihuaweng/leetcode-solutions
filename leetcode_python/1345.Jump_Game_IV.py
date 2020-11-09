# https://leetcode.com/problems/jump-game-iv/

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        d = collections.defaultdict(list)
        for i, val in enumerate(arr):
            d[val].append(i)
            
        queue = collections.deque([(0, 0)])
        seen = set()
        n = len(arr)
        
        while queue:
            i, steps = queue.popleft()
            if i == n-1:
                return steps
            
            seen.add(i)
            if i + 1 < n and i+1 not in seen:
                queue.append((i+1, steps+1))
            if i - 1 >= 0 and i-1 not in seen:
                queue.append((i-1, steps+1))
            for j in d[arr[i]]:
                if j not in seen:
                    queue.append((j, steps+1))
            del d[arr[i]]   # 优化，走过同样的就直接删除，以后不会再走
        return -1