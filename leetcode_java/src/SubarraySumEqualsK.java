package com.leetcode;

import java.util.HashMap;
import java.util.Map;

class Solution {
    public int subarraySum(int[] nums, int k) {
        int preSum = 0;
        int res = 0;
        Map<Integer, Integer> counter = new HashMap<>();
        counter.put(0, 1);
        for (int num: nums) {
            preSum += num;
            if (counter.containsKey(preSum-k)){
                res += counter.get(preSum-k);
            }
            counter.put(preSum, counter.getOrDefault(preSum, 0)+1);
        }
        return res;
    }
}

