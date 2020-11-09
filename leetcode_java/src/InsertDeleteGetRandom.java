package com.leetcode;

import java.util.ArrayList;
import java.util.HashMap;

class RandomizedSet {

    private ArrayList<Integer> nums;
    private HashMap<Integer, Integer> idx;
    private java.util.Random rand = new java.util.Random();

    /** Initialize your data structure here. */
    public RandomizedSet() {
        nums = new ArrayList<Integer>();
        idx = new HashMap<Integer, Integer>();
    }

    /** Inserts a value to the set. Returns true if the set did not already contain the specified element. */
    public boolean insert(int val) {
        if (!idx.containsKey(val)) {
            idx.put(val, nums.size());
            nums.add(val);
            return true;
        } else {
            return false;
        }
    }

    /** Removes a value from the set. Returns true if the set contained the specified element. */
    public boolean remove(int val) {
        if (idx.containsKey(val)) {
            int index = idx.get(val);
            int last = nums.get(nums.size() - 1);
            nums.set(index, last);
            nums.remove(nums.size()-1);

            idx.put(last, index);
            idx.remove(val);
            return true;
        } else {
            return false;
        }
    }

    /** Get a random element from the set. */
    public int getRandom() {
        return nums.get(rand.nextInt(nums.size()));
    }
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet obj = new RandomizedSet();
 * boolean param_1 = obj.insert(val);
 * boolean param_2 = obj.remove(val);
 * int param_3 = obj.getRandom();
 */
