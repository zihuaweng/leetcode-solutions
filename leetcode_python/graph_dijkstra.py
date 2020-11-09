#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O(E * log(V))


import heapq
import collections


def dijkstra(edges, f, t):
    g = collections.defaultdict(list)
    for s, e, c in edges:
        g[s].append((c, e))

    q = [(0, f)]
    seen = set()
    dist = {f: 0}       # 保存当前最小路径值
    prev = {f: None}    # 保存父节点用于返回path

    while q:
        (cost, v1) = heapq.heappop(q)
        if v1 == t:
            return dist[t], prev      # 提前结束
        seen.add(v1)
        # lazy dijkstra 会添加重复的node，但是cost不是最优的，这一步可以跳过重复且非最优的结果。
        # eager dijkstra 如果使用index priority queue可以避免加入重复的值，可以省略这一步
        if cost > dist.get(v1, float('inf')):   
            continue
        for c2, v2 in g[v1]:
            if v2 in seen:
                continue
            new_cost = cost + c2
            if new_cost < dist.get(v2, float('inf')):
                dist[v2] = new_cost    # 更新更短的路径
                prev[v2] = v1    # 记录上一个节点
                heapq.heappush(q, (new_cost, v2))
                    
        
    return float('inf'), prev

def function(edges, f, t):
    cost, prev = dijkstra(edges, f, t)
    path = []
    if cost == float('inf'):
        return path
    while t != None:
        path.append(t)
        t = prev[t]
    return cost, path[::-1]   # 这里注意是倒叙

if __name__ == "__main__":
    edges = [
        ("A", "B", 7),
        ("A", "D", 5),
        ("B", "C", 8),
        ("B", "D", 9),
        ("B", "E", 7),
        ("C", "E", 5),
        ("D", "E", 15),
        ("D", "F", 6),
        ("E", "F", 8),
        ("E", "G", 9),
        ("F", "G", 11)
    ]

    print("A -> E:")
    print(function(edges, "A", "E"))
    print("F -> G:")
    print(function(edges, "F", "G"))
