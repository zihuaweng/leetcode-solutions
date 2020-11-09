#!/usr/bin/env python3
# coding: utf-8

# https://leetcode.com/problems/course-schedule-ii/
# 第一种方法： dfs：
# 记录每个课程的先修课个数，以及每门课后面可以上的科目。stack里面有所有不需要先修课的课程，这些课可以任意顺序选修。
# 他们后面的课程，因为当前课程已经上完，所以先修课就减1，如果遇到有先修课已经都上完的课，证明这门课可以任意选修，加进去队列中。
# Time complexity: O(n)
# Space complexity: O(n)

class Solution1:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        class_next = collections.defaultdict(set)
        class_pre = [0 for i in range(numCourses)]
        for c, prec in prerequisites:
            class_next[prec].add(c)
            class_pre[c] += 1
        non_pre_class = [i for i in range(numCourses) if class_pre[i] == 0]
        res = []
        while non_pre_class:
            cur = non_pre_class.pop()
            res.append(cur)
            for i in class_next[cur]:
                class_pre[i] -= 1
                if class_pre[i] <= 0:
                    non_pre_class.append(i)
        if len(res) == numCourses:
            return res
        else:
            return []

# 第一种方法： bfs：
# 先使用了一个queue （python里面for循环相当于queue），如果有走过的，吧pre_class个数删除了。
# Time complexity: O(n)
# Space complexity: O(n)

# 此代码是直接在207基础上修改
# 如果判断能否上完所有课，只需要判断 numCourses == 0 （207题）
# 如果返回上课顺序，需要返回queue + 判断 numCourses == 0 （210题）

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)
        degree = collections.defaultdict(int)
        for next_class, pre_class in prerequisites:
            graph[pre_class].append(next_class)
            degree[next_class] += 1

        queue = [c for c in range(numCourses) if c not in degree]
        for cur_class in queue:
            numCourses -= 1
            for c in graph[cur_class]:
                degree[c] -= 1
                if degree[c] == 0:   # 这里不能小于零，否则重复添加内容了
                    queue.append(c)
        return queue if numCourses == 0 else []