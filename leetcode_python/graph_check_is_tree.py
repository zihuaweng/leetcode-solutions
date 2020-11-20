import collections

class Graph:
    def __init__(self):
        self.graph = collections.defaultdict(list)

    def add_edge(self, u, v):
        self.graph[v].append(u)
        self.graph[u].append(v)

    def has_cycle(self, v, visited, parent):
        visited[v] = True

        for next_node in self.graph[v]:
            if not visited[next_node]:
                if self.has_cycle(next_node, visited, v):
                    return True

            elif next_node != parent:
                return True

        return False

    def is_tree(self):
        visited = [False] * len(self.graph)
        
        if self.has_cycle(0, visited, -1):
            return False

        for i in self.graph:
            if not visited[i]:
                return False

        return True


g1 = Graph() 
g1.add_edge(1, 0) 
g1.add_edge(0, 2) 
g1.add_edge(0, 3) 
g1.add_edge(3, 4) 
print(g1.is_tree())


g2 = Graph() 
g2.add_edge(1, 0) 
g2.add_edge(0, 2) 
g2.add_edge(2, 1) 
g2.add_edge(0, 3) 
g2.add_edge(3, 4) 
print(g2.is_tree())