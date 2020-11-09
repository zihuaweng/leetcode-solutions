class Solution {
    public int maxSubArray(int[] nums) {
        if (nums.length == 0 || nums == null) {
            return 0;
        }
        int preSum = 0;
        int maxSum = Integer.MIN_VALUE;
        for (int i = 0; i < nums.length; i++) {
            preSum += nums[i];
            maxSum = Integer.max(preSum, maxSum);
            if (preSum < 0) {
                preSum = 0;
            }
        }
        return maxSum;
    }
}