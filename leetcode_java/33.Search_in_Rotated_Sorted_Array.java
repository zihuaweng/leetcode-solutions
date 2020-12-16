// https://leetcode.com/problems/search-in-rotated-sorted-array/

class Solution {
  public int search(int[] nums, int target) {
    int left = 0;
    int right = nums.length - 1;

    while (left <= right) {
      int mid = (right - left) / 2 + left;
      if (nums[mid] == target) {
        return mid;
      }

      if (nums[mid] < nums[left]) {
        if (nums[mid] < target && target <= nums[right]) {
          left = mid + 1;
        } else {
          right = mid - 1;
        }
      } else {
        if (nums[left] <= target && target < nums[mid]) {
          right = mid - 1;
        } else {
          left = mid + 1;
        }
      }
    }

    return -1;
  }
}