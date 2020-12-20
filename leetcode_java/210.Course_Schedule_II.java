// https://leetcode.com/problems/course-schedule-ii/

class Solution {
  public int[] findOrder(int numCourses, int[][] prerequisites) {
    List<List<Integer>> next = new ArrayList<>();
    int[] indegree = new int[numCourses];
    int[] order = new int[numCourses];
    int index = 0;

    for (int i = 0; i < numCourses; i++)
      next.add(new ArrayList());

    for (int[] p : prerequisites) {
      int n = p[0];
      int pre = p[1];
      next.get(pre).add(n);
      indegree[n]++;
    }

    Queue<Integer> queue = new LinkedList<>();
    for (int i = 0; i < numCourses; i++) {
      if (indegree[i] == 0) {
        queue.offer(i);
      }
    }

    while (!queue.isEmpty()) {
      int cur = queue.poll();
      order[index++] = cur;
      for (int n : next.get(cur)) {
        indegree[n]--;
        if (indegree[n] == 0) {
          queue.offer(n);
        }
      }
    }

    return index == numCourses ? order : new int[0];
  }
}