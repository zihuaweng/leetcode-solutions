class Solution {
    public int findMaxLength(int[] nums) {
        int max = 0;
        int preSum = 0;
        Map<Integer, Integer> map = new HashMap<>();
        map.put(0, -1);
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 0) {
                preSum--;
            } else {
                preSum++;
            }
            if (map.containsKey(preSum)) {
                max = Math.max(max, i-map.get(preSum));
            } else {
                map.put(preSum, i);
            }
        }
        return max;
    }
}