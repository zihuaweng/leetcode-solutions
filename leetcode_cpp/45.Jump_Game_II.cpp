// https://leetcode.com/problems/jump-game-ii/

class Solution {
 public:
  int jump(vector<int>& nums) {
    int start = 0;
    int end = 0;
    int step = 0;
    if (nums.size() == 1) {
      return 0;
    }

    while (start <= end) {
      int new_end = 0;
      for (int i = start; i <= end; i++) {
        new_end = max(new_end, nums[i] + i);
        if (new_end >= nums.size() - 1) {
          return ++step;
        }
      }
      step++;
      start = end + 1;
      end = new_end;
    }
    return -1;
  }
};