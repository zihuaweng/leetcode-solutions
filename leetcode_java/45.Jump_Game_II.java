// https://leetcode.com/problems/jump-game-ii/

class Solution {
  public int jump(int[] nums) {
    int start = 0;
    int end = 0;
    int step = 0;

    if (nums.length == 1) {
      return 0;
    }

    while (start <= end) {
      int new_end = 0;
      for (int i = start; i <= end; i++) {
        new_end = Math.max(new_end, i + nums[i]);
        if (new_end >= nums.length - 1) {
          return ++step;
        }
      }
      step++;
      start = end + 1;
      end = new_end;
    }

    return -1;
  }
}