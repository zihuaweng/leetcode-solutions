// https://leetcode.com/problems/container-with-most-water/submissions/

class Solution {
  public int maxArea(int[] height) {
    int left = 0;
    int right = height.length - 1;

    int res = 0;

    while (left < right) {
      int w = right - left;
      int h = Math.min(height[left], height[right]);
      res = Math.max(res, w * h);

      if (height[left] <= height[right]) {
        left++;
      } else {
        right--;
      }
    }

    return res;
  }
}