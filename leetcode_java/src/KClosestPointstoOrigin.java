package com.leetcode;

import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.Stack;

class Solution {
    public int[][] kClosest(int[][] points, int K) {

        PriorityQueue<int []> heap = new PriorityQueue<int[]>(new Comparator<int[]>() {
            @Override
            public int compare(int[] left, int[] right) {
                return getDistance(right) - getDistance(left);
            }
        });

        for (int[] point: points) {
            heap.add(point);
            if (heap.size() > K) {
                heap.poll();
            }
        }

        int[][] res = new int[K][2];
        while (K>0) {
            res[--K] = heap.poll();
        }
        return res;
    }

    private int getDistance(int[] point) {
        return point[0] * point[0] + point[1] * point[1];
    }

    Stack<Character>
}