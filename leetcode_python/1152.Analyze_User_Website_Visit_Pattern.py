#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/analyze-user-website-visit-pattern/

class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        webs = collections.defaultdict(list)
        for t, u, w in sorted(zip(timestamp, username, website)):
            webs[u].append(w)

        counter = collections.Counter()
        for user, websites in webs.items():
            counter += collections.Counter(set(itertools.combinations(websites, 3)))

        sorted_counter = sorted(counter, key=lambda x: (-counter[x], x))
        return sorted_counter[0]