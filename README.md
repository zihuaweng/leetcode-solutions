# Leetcode Solutions

This repo contains my solutions and notes for 600+ leetcode questions mainly in Python. I plan to switch to C++, so more solutions in C++ will be added in the future.

## Recommended Resources
### Book
1. Introduction to algorithms
1. [Competitive Programmer's Handbook](https://cses.fi/book/book.pdf)

### YouTube
1. [Google Engineer Explains](https://www.youtube.com/channel/UClPLjM6vk6sjd1OuFSoxx-Q), great materials to study how to approach coding interviews.
1. [Huifeng Guan](https://www.youtube.com/channel/UCY5Z0of98W-YSdmPgAe1DaA), 每日一题. The best leetcode practice channel ever.
1. [William Lin](https://www.youtube.com/channel/UCKuDLsO0Wwef53qdHPjbU2Q), just for fun. Take a break and think about what stupid I am :)
1. [WilliamFiset](https://www.youtube.com/channel/UCD8yeTczadqdARzQUp29PJw), his graph theory playlist is a must-watch for beginners in my opinion.  

## Algorithms
1. [Rolling Hashing](https://www.youtube.com/watch?v=BQ9E-2umSWc)
2. [Rabin–Karp algorithm](https://en.wikipedia.org/wiki/Rabin%E2%80%93Karp_algorithm)
    - String-searching algorithm uses hashing to **find an exact match of a pattern string in a text**. It uses a **rolling hash** to quickly filter out positions of the text that cannot match the pattern, and then checks for a match at the remaining positions. Generalizations of the same idea can be used to find more than one match of a single pattern, or to find matches for more than one pattern.
    - two steps: first hashing two substrings, if they have the same hash value, check each character if they match.
3. [Kadane’s Algorithm, DP,](https://medium.com/@rsinghal757/kadanes-algorithm-dynamic-programming-how-and-why-does-it-work-3fd8849ed73d#:~:text=Kadane's%20algorithm%20is%20able%20to,runtime%20of%20O(n).)
    - DP, Maximum Subarray Problem
4. [Floyd's cycle-finding algorithm](https://en.wikipedia.org/wiki/Cycle_detection)
    - Find the starting point of cycle/graph
    - Find cycle linked list, find duplicated number in a list
    - [explanation video](https://www.youtube.com/watch?v=9YTjXqqJEFE)
5. [Eulerian path](https://en.wikipedia.org/wiki/Eulerian_path#:~:text=An%20Eulerian%20cycle%2C%20Eulerian%20circuit,every%20vertex%20has%20even%20degree.)
    - Eulerian trail (or Eulerian path) is a trail in a finite graph that visits every edge exactly once (allowing for revisiting vertices).
    - Eulerian circuit or Eulerian cycle is an Eulerian trail that starts and ends on the same vertex.
    ```
    Given the graph in the image, is it possible to construct a path (or a cycle; i.e., a path starting and ending on the same vertex) that visits each edge exactly once?
    ```
6. [Topological sorting](https://en.wikipedia.org/wiki/Topological_sorting)
    - A topological sort or topological ordering of a directed graph is a linear ordering of its vertices such that for every directed edge uv from vertex u to vertex v, u comes before v in the ordering.
    - The graph must be Directed Acyclic Graph (DAG).
    - For instance, the vertices of the graph may represent tasks to be performed, and the edges may represent constraints that one task must be performed before another; in this application, a topological ordering is just a valid sequence for the tasks.
    - Find Eulerian path, school class prerequisites, visit location order
    - [Code](https://github.com/zihuaweng/leetcode-solutions/blob/master/leetcode_python/graph_topological_sort.py)
    
7. [Karnaugh Maps](https://en.wikipedia.org/wiki/Karnaugh_map)
    - The Karnaugh map (KM or K-map) is a method of simplifying Boolean algebra expressions.
    - [Video](https://www.youtube.com/watch?v=RO5alU6PpSU)

8. knapsack question
    - Select a subset from an array where their sum equals a target



## Category
### Graph
#### Representation
1. Adjacency Matrix
    - Pros
        - Space efficient for reprenseting dense graphs (have a lot edges)
        - Edge weight lookup is O(1)
        - Simplest graph representation
    - Cons
        - Space O(V^2)
        - Iterating over all edges takes O(V^2)

2. Adjacency List
    - Pros
        - Space efficient for representing sparse graphs (have a lot nodes)
        - Iterating over all edges is efficient
    - Cons
        - Less space-efficient for representing dense graphs
        - Edge lookup is O(E)
        - slightly more complex graph representation

#### DFS
1. Marks node as seen(grid[i][j] = '2' or seen.add(i)) at the beginning of dfs and check boundaries, seen, and the condition for the next loop (grid[x][y] == '1')
    ```python
    200. number of islands

    class Solution:
        def numIslands(self, grid: List[List[str]]) -> int:
            count = 0
            if not grid:
                return 0
            m = len(grid)
            n = len(grid[0])

            for i in range(m):
                for j in range(n):
                    if grid[i][j] == '1':
                        count += 1
                        self.dfs(grid, i, j)
            return count

        def dfs(self, grid, i, j):
            grid[i][j] = '2'  # marks seen first
            for _x, _y in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                x = i + _x
                y = j + _y
                if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == '1':
                    self.dfs(grid, x, y)
    ```
1. 如果dfs需要判断上一层的结果并返回，则把边界放到判断后面，下一个dfs遍历之前。
    ```python
    79. word search

    def dfs(self, board, i, j, word):
        if not word:
            return True
        # 因为这里有判断，这个word是又前面的dfs生成的，对边界的判断应该放在最前面，如果没有判断word，例如计算island个数
        # 那样的可以放在生成了新的x,y后面立马判断。
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return
        if board[i][j] == "#" or board[i][j] != word[0]:  # Checks seen and next loop condition
            return False
        temp = board[i][j]
        board[i][j] = "#"    # backtrack， marks node as seen
        for x, y in [(i, j + 1), (i, j - 1), (i + 1, j), (i - 1, j)]:
            if self.dfs(board, x, y, word[1:]):
                return True
        board[i][j] = temp
        return FalseF
    ```
2. 使用memorization保存前面的计算
    - 如果是单个node的visits，直接使用dict
    - 如果是组合的dfs，例如Campus Bikes II，可以使用状态压缩，binary来保存key
        ```python
        # Thre is 1<<n valid status
        mo = [0] * (1<<n)  

        # ---------------
        if mo[state] != 0:
            return mo[state]

        if state & (1<<j) == 0:  # This condition means j is not visited
            st = state | (1<<j)  # Adds j and creates new status
            res = dfs(st, xxxx)

        mo[state] = res
        return res
        ```

#### BFS
1. A regular bfs uses queue to store nodes. Adds new node to queue and marks it as seen at the same time.
    ```python
    def bfs(self, grid, r, c):
            queue = collections.deque()
            queue.append((r, c))
            grid[r][c] = '0'    # Marks cur node as seen to avoid duplicated node in queue
            while queue:
                directions = [(0,1), (0,-1), (-1,0), (1,0)]
                r, c = queue.popleft()
                for d in directions:
                    nr, nc = r + d[0], c + d[1]    
                    if self.is_valid(grid, nr, nc) and grid[nr][nc] == '1':
                        queue.append((nr, nc))
                        grid[nr][nc] = '0'   # Marks cur node as seen to avoid duplicated node in queue
    ```
2. Calculates number of paths
    ```python
    def shortestPathBinaryMatrix(grid):
        n = len(grid)
        if grid[0][0] or grid[n-1][n-1]:
            return -1
        q = collections.deque([(0, 0, 1)])
        while q:
            i, j, d = q.popleft()
            if i == n-1 and j == n-1: 
                return d
            for x, y in ((i-1,j-1),(i-1,j),(i-1,j+1),(i,j-1),(i,j+1),(i+1,j-1),(i+1,j),(i+1,j+1)):
                if 0 <= x < n and 0 <= y < n and not grid[x][y]:
                    grid[x][y] = 1   # Marks cur node as seen before next loop
                    q.append((x, y, d+1))
        return -1
    ```

#### Union Find
1. Union Find
    ```python
    323. Number of Connected Components in an Undirected Graph

    parent = [x for x in range(n)]

    def find(x):  
        if parent[x] != x:
            parent[x] = find(parent[x])    # path compression
        return parent[x]

    def union(x, y):
        p_x = find(x)
        p_y = find(y)
        if p_x != p_y:               
            parent[p_y] = p_x
            
    for u, v in edges:
        union(u, v)
    ```

2. Union Find By Rank
    ```python
    parent, rank = {}, {}
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        x, y = find(x), find(y)
        if x != y:
            if rank[x] < rank[y]:
                x, y = y, x
            parent[y] = x
            rank[x] += rank[x] == rank[y]
    ```

#### Critical Connections
需要找到critical-connections就是需要找不在环上面的边，他们都是critical-connections。所以我们走graph，然后记录rank，如果子节点的rank比当前节点的rank更小，证明当前是环内的连接，连到了原来走过的节点。我们更新当前节点到最小值。如果子节点最后的rank是当前rank+1，证明这是一个线性的连接，就是critical-connections。
- [Code](https://github.com/zihuaweng/leetcode-solutions/blob/master/leetcode_python/graph_critical_connections.py)
- [Leetcode question example No.1192](https://github.com/zihuaweng/leetcode-solutions/blob/master/leetcode_python/1192.Critical_Connections_in_a_Network.py)

#### Find Cycle in Directed Graph
- [Code](https://github.com/zihuaweng/leetcode-solutions/blob/master/leetcode_python/graph_find_cycle.py)

#### Strongly Connected Component
1. Tarjan's
    - [Video](https://www.youtube.com/watch?v=wUgWX0nc4NY)
    - [Code](https://github.com/zihuaweng/leetcode-solutions/blob/master/leetcode_python/graph_strongly_connected_component.py)
    - O(V+E)

#### Critical Connections, Bridge
- [Video](https://www.youtube.com/watch?v=aZXi1unBdJA)
- [Code](https://github.com/zihuaweng/leetcode-solutions/blob/master/leetcode_python/graph_critical_connections.py)
- O(V+E)

#### Shortest Path Problem
1. BFS (unweighted graph)
    - O(E + V)
2. Dijkstra's (non-negative acycles)
    - Only works for non-negative weights DAG
    - O((E+V)*LogV) = O(ELogV)
    - [Code](https://github.com/zihuaweng/leetcode-solutions/blob/master/leetcode_python/graph_dijkstra.py)
3. Bellman-Ford (negative cycles)
    - Works if there is negative weight path, it could use to detect negative cycle
    - Steps
        - set all node dist to inf
        - set dist[start] to 0
        - relax each edge V-1 times
    - Code
        ```python
        for i in range(V-1):
            for edge in edges:
                # update the node to the shortest path
                if edge.start + cost < edge.to:
                    edge.to = edge.start + cost

        # find nodes in the negative cycle, just loop the graph again
        for i in range(V-1):
            for edge in edges:
                # update the node to the shortest path
                if edge.start + cost < edge.to:
                    edge.to = float('-inf)
        ```
    - The time complexity of the algorithm is O(nm), because the algorithm consists
of n−1 rounds and iterates through all m edges during a round. If there are no
negative cycles in the graph, all distances are final after n −1 rounds, because
each shortest path can contain at most n−1 edges

4. Floyd-Warshall
    - It finds all shortest paths between the nodes in a single run, using dp to solve it and returns the shortest dist between two arbitrary nodes. 
    - Maintain a two-dimensional array that contains distances between the nodes. First the distances are calculated only using direct edges between nodes, and then the algorithm reduces disatances by using intermidiate nodes in the paths
    - dp[i][j] == dist between i, j, we need to know if there is an intermidiate node k that dp[i][j] > dp[i][k] + dp[k][j], if yes, update the dist and it is the shorter path.
    - Code
        ```python
        # initialze the dp first
        n = len(V)
        dp = [[float('inf')] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i == j: dp[i][j] = 0 # node to itself has dist == 0
                elif j in graph[i]: dp[i][j] = graph[i][j] # pupulate the cost

        # update dp in a single run
        for k in range(n):   # k is the intermidiate node
            for i in range(n):
                for j in range(n):
                    dp[i][j] = min(dp[i][j], dp[i][k]+dp[k][j])
        ```
    - Time O(n^3), only use it when the graph is small
    - Space O(n^2)

5. A*

#### Connectivity
1. Union find
    - Counting Number of connections using graph
2. DFS / BFS

#### Negative Cycles
1. Bellman-Ford
2. Floyd-Warshall

### Traveling Salesman Problem
1. Held-Karp
2. Branch and bound

#### Topological Sort 
1. Applications: Get the order of graph: class prerequisites, program dependencies. 
1. Does not work for graphs with cycle
1. Algorithm 1 dfs:
    - Pick an unvisited node
    - Begin with the selected node, do a dfs, exploring only unvisited nodes.
    - On the recursive callback of dfs, add the current node to list
    - Reverse the list
1. Algorithm 2 Kahn's Algorithm:
    - Count in degree for all node
    - Add nodes with in-degree == 0 to queue
    - Walkthrough the queue, add the current node to result, decrease the indegree for the next node, if indegree == 0, add to the queue.
1. [Code](https://github.com/zihuaweng/leetcode-solutions/blob/master/leetcode_python/graph_topological_sort.py)
1. O(E+V)

#### Eulerian Paths and Circuits
1. Eulerian Path is a path that visits all edges in a graph exactly once
2. Eulerian Circuit is an Eulerian Path that starts and ends on the same vertex
3. Algorithm: if we can find the path, we can find the circuit
    - Verify if the graph has an eulerian path.
    - Find the start vertex
    - Dfs
    - Return path if len(path) == len(edges) + 1
4. [Code](https://github.com/zihuaweng/leetcode-solutions/blob/master/leetcode_python/graph_eulerian_path.py)
5. [Leetcode question example No.332](https://leetcode.com/problems/reconstruct-itinerary/)


### Tree
#### Center of Undirected Tree
1. The center is always the middle vertex or middle two vertices in every longest path along the tree.
    - Get the middle of the longest path
2. Another way is to iteratively pick off each leaf node layer like we're peeling an onion.
    - Computer the degree of each node. Each node will have a degree of 1
    - Prune nodes also reduce the node degree
    - [Code](https://github.com/zihuaweng/leetcode-solutions/blob/master/leetcode_python/tree_find_center.py)
3. [Video](https://www.youtube.com/watch?v=nzF_9bjDzdc&list=PLDV1Zeh2NRsDGO4--qE8yH72HFL1Km93P&index=10)
3. O(V+E)

#### Identifying Isomorphic Trees
1. Get the center of both trees
2. Root both trees and encode them.
    - Encode: we use '()' to represent one node. If one node has two children. it should be '(()())', if it only has one child, it should be '(())'. When we create the tree parent encoding, the child needs to be sorted. '((())())' is correct but not '(()(()))'
3. Compare the encode tree. We need to root the other tree using all the centers, since we might have two tree center.
4. Code
    ```python
    def is_isomorphic(tree1, tree2):
        if not tree1 or not tree2:
            return

        center1 = find_tree_center(tree1)
        center2 = find_tree_center(tree2)

        rooted_tree1 = root_tree(tree1, center1[0])  # dosen't matter which center
        encoded_tree1 = encode_tree(rooted_tree1)

        for center in center2:
            rooted_tree2 = root_tree(tree2, center)
            encoded_tree2 = encode_tree(rooted_tree2)
            if encoded_tree1 == encoded_tree2:
                return True
        return False
    ```


### Two Pointers
1. Sliding Window Problems
    - 1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
    - 1425. Constrained Subsequence Sum
    - 1358. Number of Substrings Containing All Three Characters
        - 需要知道怎么才能累加所有可能不漏掉 res += i
    - 1248. Count Number of Nice Subarrays
        - subarray, 如果是at most k distinct的话，可以使用sliding window，但是是extract k distinct的话，就需要用atMost(k)-atMost(k-1)
    - 1234. Replace the Substring for Balanced String
        - 需要替换其中的subarray，判断条件就是滑窗外面的count，注意index区间会out of range
    - 1004. Max Consecutive Ones III
    - 930. Binary Subarrays With Sum
        - 第一种方法使用pre_sum dict
        - 第二种方法，subarray, 如果是at most k distinct的话，可以使用sliding window，但是是extract k distinct的话，就需要用atMost(k)-atMost(k-1)
    - 992. Subarrays with K Different Integers
        - subarray, 如果是at most k distinct的话，可以使用sliding window，但是是extract k distinct的话，就需要用atMost(k)-atMost(k-1)
    - 159. Longest Substring with At Most Two Distinct Characters
        - subarray, 保存一个freq的dict
    - 862. Shortest Subarray with Sum at Least K
        - 参照239. Sliding Window Maximum， 239是维护一个递减queue
        - subarray, 与209差别是包含负数, 维护一个递增的pre_sum queue
    - 209. Minimum Size Subarray Sum
        - subarray, 所有是正数，所以滑动窗口，sum是累加的，通过右边加，左边减，可以得到结果


### Stack
1. Monotonic stack
    - Constrained Subsequence Sum
    - Minimum Cost Tree From Leaf Values  #### star question
    - Sum of Subarray Minimums
    - Online Stock Span
    - Score of Parentheses
    - Next Greater Element II
    - Next Greater Element I
    - Largest Rectangle in Histogram
    - Trapping Rain Water

### Calculate Four Directions
```python
# up
dx, dy = 0, 1
# right
dx, dy = dy, -dx
# left 
dx, dy = -dy, dx
# down
dx, dy = dx, -dy

diagonal

row == col
row+col == size-1
```

### Binary Search
- [Video](https://www.youtube.com/watch?v=UyFShaHNbNY)
- [Template](https://github.com/zihuaweng/leetcode-solutions/blob/master/leetcode_python/binary_search_example.py)


### Leetcode Questions
1. Complete search
    - Generating subsets: 使用二进制0101011 （ 0:1<<n -1）生成组合，然后生成subset
    - Pruning the search: 矩阵能走过每个点一次的路径数量，可以优化：
        - 只需要走一遍，对称另一边 * 2，确保第一步一定是走同一个方向即可
        - 提前走到终点，该路径不符合条件
        - 如果走到一个点只能选两个方向中一个，证明一定会有另一边的路径不能走到，该路径不符合条件
    - Meet in the middle: 将任务分成两组，对于2^n任务来说可以优化时间
    - Permutations:
    ```python
    # Function to print permutations of a string 
    # This function takes three parameters: 
    # 1. String 
    # 2. Starting index of the string 
    # 3. Ending index of the string. 
    def permute(a, l, r): 
        if l==r: 
            print toString(a) 
        else: 
            for i in xrange(l,r+1): 
                a[l], a[i] = a[i], a[l] 
                permute(a, l+1, r) 
                a[l], a[i] = a[i], a[l] # backtrack 


    # Python function to print permutations of a given list 
    def permutation(lst): 
  
        # If lst is empty then there are no permutations 
        if len(lst) == 0: 
            return [] 
    
        # If there is only one element in lst then, only 
        # one permuatation is possible 
        if len(lst) == 1: 
            return [lst] 
    
        # Find the permutations for lst if there are 
        # more than 1 characters 
    
        l = [] # empty list that will store current permutation 
    
        # Iterate the input(lst) and calculate the permutation 
        for i in range(len(lst)): 
        m = lst[i] 
    
        # Extract lst[i] or m from the list.  remLst is 
        # remaining list 
        remLst = lst[:i] + lst[i+1:] 
    
        # Generating all permutations where m is first 
        # element 
        for p in permutation(remLst): 
            l.append([m] + p) 
        return l 
    ```


2. Greedy Algorithms
Constructs a solution to the problem by always making a choice that looks the best at the moment.
    - Scheduling，计算可以去的最多的meeting：每次选择结束最早的meeting
    - Tasks and deadlines，每次选择耗时最短的
    - Data compression：使用不同长度编码，频率最高的编码成最短的（0），频率较高的编码成较长的（10， 110），但是每个编码不能prefix相同。使用 Huffman coding。


3. Dynamic programming
[DP summary from Huifeng](https://docs.google.com/presentation/d/1f1gLTRmQTBxvZzHjlGzrMv8aHdNnCMilKm72Rxlptmk/edit)
Combines the correctness of complete search and the efficiency of greedy algorithms.

    - 使用场景
        - Finding an optimal solution
        - Counting the number of solutions
        - 下一个结果只依赖前一个结果
        - 将大问题拆成几个小问题，且满足无后效性， 最优子结构性质。
    - coin problem：
        - 一组subset的sum需要等于一个target  （从0到target，当前k只会依赖于target-k的结果）
        - 多少组subset的sum可以等于一个target  （从0到target，当前k只会依赖于target-k的结果）
    - Longest increasing subsequence
        - 当前increasing subsequence的长度只取决于前面最大值比他小subset的长度
        - O(nlogn)
    - Paths in a grid
        - 从矩阵的左上角走到右下角，只能往右或者下边走，当前结果只取决于左边结果和上边结果
    - Knapsack problems
        - The term knapsack refers to problems where a set of objects is given, and
subsets with some properties have to be found. 
        - 给一个数组，求出符合条件的subset， [1,3,3,5], 求出sum==12 的subset
        - 每个点都可以选择取或者不取，当前和k （0<k<=sum）只取决于取当前值（k-current）或者不取当前值结果（前一个到达k的结果）
        - possible(x,k) = possible(x−wk,k −1)∨possible(x,k −1)
        - 可以用于计算给定weight，value选择subset
    - Edit distance
        - 当前点只取决于与前一个比较，删减，添加，还是替换
        - distance(a,b) = min(distance(a,b −1)+1, distance(a−1,b)+1, distance(a−1,b −1)+cost(a,b))

4. Amortized Analysis
    - Stack， Monotonic stack
        - Nearest smaller elements
            - 需要返回每个数最近的最小值，1 3 4 2 5 3 4 2 -> 0 1 3 1 2 2 3 1
            - 规律：当后面出现有更小的值k，前面的比k大的所有数都不需要考虑
            - 维护一个单调栈 1 3 4 2 -> stack: 1 2，因为中间3，4以后都不会使用上
        - Sliding window minimum
            - 返回每个Sliding window的最小值
            - 规律：当后面出现有更小的值k，前面的比k大的所有数都不需要考虑
            - 维护一个Sliding window里的单调栈


5. Range Queries
    - sum(a,b): calculate the sum of values in range [a,b]
        - for static array, use pre sum
    - min(a,b): find the minimum value in range [a,b]
        - The idea is to precalculate all values of minq(a,b) where b − a +1 (the length
of the range) is a power of two. For example, for the array
        - The number of precalculated values is O(nlogn) using recursive formula: minq(a,b) = min(minq(a,a+w−1),minq(a+w,b))
        - Get result in O(1): Let k be the largest power of two that does not exceed
b − a+1, minq(a,b) = min(minq(a,a+ k −1),minq(b − k +1,b)).

    - Binary indexed tree (对需要更新的list，logn更新, logn计算区间sum)
        - can be seen as a dynamic variant of a prefix sum array
        - O(logn) time operations on return array sum and updating a value.
        - [Link](https://www.topcoder.com/community/competitive-programming/tutorials/binary-indexed-trees/)

    - Segment tree
        - support updating an array value, support sum queries, minimum and maximum queries in O(logn) time
        - is a more general data structure than binary index tree

    - Index compression
        - if we know all the indices needed during the algorithm beforehand
        - find a function c for c(a) < c(b) where a < b  [c(8) = 1, c(555) = 2, c(109
) = 3]
        - use to save space
