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
          "wrt",
          "wrf",
          "er",
          "ett",
          "rftt"
          
          t < f
          w < e
          r < t
          e < r
          w < f
          
          t f w e r 
          1 2   1 1
          
          wertf
          
          topological sort
          1. build graph:
            1. compare the word, get the first index with diff char in both words
                1. prev -> next
                2. indegree[next] += 1, defaultdict, default is 0
          2. get order 
            1. create a queue with indegree[node] == 0
            1. visit nodes in queue
                add node to the result
            2. visit the next node
                indegree[next] -= 1
                if indegree[next] == 0, add the node to the queue
                
        corner case:
            1. has cycle: order is invalid, return empty
            2. len(words) <= 1: return empty
            3. len(prev) > len(next), and next.startswith(prev): return empty
                
        """
        # build graph
        graph = collections.defaultdict(set)
        indegree = {}
        for word in words:
            for c in word:
                indegree[c] = 0  # need to have get the indegree[node] == 0
        
        for i in range(1, len(words)):
            first = words[i-1]
            second = words[i]
            if len(first) > len(second) and first.startswith(second):
                return ''
            
            for j in range(min(len(first), len(second))):
                if first[j] != second[j]:
                    if second[j] not in graph[first[j]]:
                        graph[first[j]].add(second[j])
                        indegree[second[j]] += 1
                    break
                    
        # get order
        queue = [node for node in indegree if indegree[node] == 0]
        res = ''
        for node in queue:
            res += node
            for next_node in graph[node]:
                indegree[next_node] -= 1
                if indegree[next_node] == 0:
                    queue.append(next_node)
                    
        # check cycle
        if len(res) == len(indegree):
            return res
        return ''