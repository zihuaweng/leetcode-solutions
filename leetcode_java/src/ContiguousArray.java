// https://leetcode.com/problems/contiguous-array/


class Solution {
    public int findMaxLength(int[] nums) {
        int length = 0;
        if (nums == null || nums.length == 0) {
            return length;
        }
        HashMap<Integer, Integer> count = new HashMap<>();
        count.put(0,0);
        int sum = 0;
        for (int i=1; i<=nums.length; i++) {
            if (nums[i-1] == 0) {
                sum -= 1;
            }
            if (nums[i-1] == 1) {
                sum += 1;
            }
            if (count.containsKey(sum)) {
                length = Math.max(length, i-count.get(sum));
            } else {
                count.put(sum, i);
            }
        }
        return length;
    }
}