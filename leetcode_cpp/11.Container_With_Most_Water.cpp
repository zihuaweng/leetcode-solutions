// https://leetcode.com/problems/container-with-most-water/submissions/

class Solution {
 public:
  int maxArea(vector<int>& height) {
    int left = 0;
    int right = height.size() - 1;

    int temp = 0;

    while (left < right) {
      int w = right - left;
      int h = min(height[left], height[right]);
      temp = max(temp, w * h);

      if (height[left] >= height[right]) {
        right--;
      } else {
        left++;
      }
    }

    return temp;
  }
};