#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O(n*m) account长度 * email个数
# Space complexity: O(n)

# 合并问题要想到图结构
# https://leetcode.com/problems/accounts-merge/

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        name_map = {}
        graph = {}
        # 构建无向图
        for account in accounts:
            name = account[0]
            for i in range(1, len(account)):
                name_map[account[i]] = name
                if account[i] not in graph:
                    graph[account[i]] = set()
                if i != 1:
                    graph[account[i]].add(account[i - 1])
                    graph[account[i - 1]].add(account[i])
        # dfs
        res = []
        seen = set()
        for email in graph:
            if email not in seen:
                seen.add(email)
                temp = [email]
                self.dfs(seen, graph, email, temp)
                temp = [name_map[temp[0]]] + sorted(temp)
                res.append(temp)

        return res

    def dfs(self, seen, graph, email, temp):
        for e in graph[email]:
            if e not in seen:
                temp.append(e)
                seen.add(e)
                self.dfs(seen, graph, e, temp)


# 另一种方法， union found

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = {}
        name_map = {}

        def find(i):
            if parent[i] != i:
                parent[i] = find(parent[i])
            return parent[i]

        def union(i, j):
            parent[find(i)] = find(j)

        for account in accounts:
            name = account[0]
            for email in account[1:]:
                if email not in parent:
                    parent[email] = email
                name_map[email] = name
                union(email, account[1])

        res = collections.defaultdict(list)
        for email in parent.keys():
            res[find(email)].append(email)

        return [[name_map[e]] + sorted(emails) for e, emails in res.items()]