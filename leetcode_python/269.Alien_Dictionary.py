#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/alien-dictionary/
# 首先构建图
# 打印拓扑结构

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        """
        1. build graph
            find the order
        wrt wrf.  t -> f
        er ett   r->t
        w -> e
        e->r
        
        compare each word with the next word, find the first diff char
    
        2. topological sort
            count indegree for each char
            start with node with 0 indegree, -1 if we visit the node
            keep adding node with 0 indegree
        w e r t f
        
        """
        # build graph
        in_degree = {}        
        for w in words:
            for c in w:
                in_degree[c] = 0    # important for ['z', 'z'] case
                
        graph = collections.defaultdict(set)
        for i in range(1, len(words)):
            a = words[i-1]
            b = words[i]
            if len(a) > len(b) and a.startswith(b):
                return ''
            for j in range(min(len(a), len(b))):
                if a[j] != b[j]:
                    if b[j] not in graph[a[j]]:   # in case we add duplicated keys
                        graph[a[j]].add(b[j])
                        in_degree[b[j]] += 1
                    break
                        
        # read graph
        queue = [w for w, count in in_degree.items() if count == 0]
        for q in queue:
            for c in graph[q]:
                in_degree[c] -= 1
                if in_degree[c] == 0:
                    queue.append(c)
                    
        return ''.join(queue) if len(queue) == len(in_degree) else ""