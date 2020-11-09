# https://leetcode.com/problems/course-schedule/
# https://blog.csdn.net/fuxuemingzhu/article/details/82951771
# 拓扑排序 ， dfs
# 这个题目目标是寻找一个有向无环图，如果有，则不能完成所有课程，如果没有则可以完成所有课程
# 判断DAG 有向无环图，需要从没有入度的vertices开始，一边读，一边吧新的没有入度数的vertices加入

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        degree = collections.defaultdict(int)
        for next_class, pre_class in prerequisites:
            graph[pre_class].append(next_class)
            degree[next_class] += 1

        queue = collections.deque([c for c in range(numCourses) if c not in degree])
        while queue:
            cur_class = queue.popleft()
            numCourses -= 1
            for c in graph[cur_class]:
                degree[c] -= 1
                if degree[c] == 0:
                    queue.append(c)
        return numCourses == 0