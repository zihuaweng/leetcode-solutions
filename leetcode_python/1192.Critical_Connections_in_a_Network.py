# https://leetcode.com/problems/critical-connections-in-a-network/
# space: O(n)
# time: O(n)

# 需要找到critical-connections就是需要找不在环上面的边，他们都是critical-connections。
# 所以我们走graph，然后记录rank，如果子节点的rank比当前节点的rank更小，证明当前是环内的连接，连到了原来走过的节点。我们更新当前节点到最小值
# 如果子节点最后的rank大于等于当前rank+1，证明这是一个线性的连接，就是critical-connections

# https://www.youtube.com/watch?v=mKUsbABiwBI

class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        """
        find the critical connection 
                    -> edges that not in a cycle
                    -> OR when deleted, we get one more group


        # need to find cycle
            1. using rank, for one more step, the rank add 1
            2. if there is a cycle, the node is visited, the rank or next edge != rank + 1

        2 -> 0 -> 1     -> 3
        0.   1    2        3
        2 -> 0 -> 1     -> 2
        0.   1    2        0               
        0    0    0

        # return edges that are not in cycle
            1. return connection: next_rank = cur_rank + 1

        time O(n)
        space O(n)
        """
        g = collections.defaultdict(set)
        for u,v in connections:
            g[u].add(v)
            g[v].add(u)
            
        res = []
        ranks = [-1] * n
        
        
        def dfs(i, prev, level):
            ranks[i] = level
            for next_node in g[i]:
                if next_node == prev:    # 跳过父节点
                    continue
                if ranks[next_node] == -1:        # 只需要遍历没有visited过的
                    dfs(next_node, i, level+1)    
                # 上一步递归会把赋值更小的rank，如果子节点有更小的，意味有一个环，那么当前节点应该选择其中的最小值
                ranks[i] = min(ranks[i], ranks[next_node])
                # 如果下一个点的rank不是level+1，证明该连接没有环，就是Critical Connection
                if ranks[next_node] >= level+1:
                    res.append([i, next_node])
        
        dfs(0, -1, 0)
        return res