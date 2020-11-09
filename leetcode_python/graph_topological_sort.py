import collections

def topological_sort_Kahn(g):
    n = len(g)
    in_degree = [0] * n
    for i in range(n):
        for j in g[i]:
            in_degree[j] += 1
    
    queue = collections.deque([i for i, c in enumerate(in_degree) if c == 0])
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for next_node in g[node]:
            in_degree[next_node] -= 1
            if in_degree[next_node] == 0:
                queue.append(next_node)
    if len(order) != n:
        return None
    return order


def topological_sort_dfs(g):
    n = len(g)
    seen = set()
    order = []
    
    def dfs(node):
        seen.add(node)
        for next_node in g[node]:
            if next_node not in seen:
                dfs(next_node)
        order.append(node)
        
    for i in range(n):
        if i not in seen:
            dfs(i)
    return order[::-1]


graph = {
    0:[2,3,6],
    1:[4],
    2:[6],
    3:[1,4],
    4:[5,8],
    5:[],
    6:[7,11],
    7:[4,12],
    8:[],
    9:[2,10],
    10:[6],
    11:[12],
    12:[8]
}

print(topological_sort_dfs(graph))