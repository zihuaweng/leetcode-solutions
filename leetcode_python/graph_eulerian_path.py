import collections
def find_eulerican_path(g):
    in_degree = [0] * len(g)
    out_degree = [0] * len(g)

    for u, v in g.items():
        out_degree[u] += len(v) 
        for n in v:
            in_degree[n] += 1

    # verify if there is a eulerican path
    if not graph_has_eulerican_path(in_degree, out_degree):
        return []

    # get start node
    start = find_start_node(in_degree, out_degree)

    res = []
    
    def dfs(start):
        while out_degree[start] != 0:
            out_degree[start] -= 1
            next_node = g[start][out_degree[start]]
            dfs(next_node)
        res.append(start)   # backtrack

    dfs(start)

    return res[::-1]  # because we add it reversely

def graph_has_eulerican_path(in_degree, out_degree):
    start_nodes = end_nodes = 0
    for i in range(len(in_degree)):
        if in_degree[i] - out_degree[i] > 1 or out_degree[i] - in_degree[i] > 1:
            return False
        elif out_degree[i] - in_degree[i] == 1:
            start_nodes += 1
        elif in_degree[i] - out_degree[i] == 1:
            end_nodes += 1
    return end_nodes == start_nodes and (end_nodes == 1 or end_nodes == 0)


def find_start_node(in_degree, out_degree):
    start = 0
    for i in range(len(in_degree)):
        # this is the uniq starting node
        if out_degree[i] == in_degree[i] + 1:
            return i
        # otherwise, start at any node with an outgoing edge
        if out_degree[i] > 0:
            start = i
    return start

graph = {0:[],
        1:[2, 3],
        2:[2, 4, 4],
        3:[1, 2, 5],
        4:[3, 6],
        5:[6],
        6:[3]}

print(find_eulerican_path(graph))