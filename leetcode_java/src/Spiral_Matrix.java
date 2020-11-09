package com.leetcode;

import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        List<Integer> res = new ArrayList<>();
        if (matrix.length == 0 || matrix[0].length == 0) {
            return res;
        }
        int m = matrix.length;
        int n = matrix[0].length;
        int up = 0;
        int down = m-1;
        int left = 0;
        int right = n-1;
        while (up < down && left < right) {
            for (int i=left; i<right; i++) {
                res.add(matrix[up][i]);
            }
            for (int i=up; i<down; i++) {
                res.add(matrix[i][right]);
            }
            for (int i=right; i>left; i--) {
                res.add(matrix[down][i]);
            }
            for (int i=down; i>up; i--) {
                res.add(matrix[i][left]);
            }
            up++;
            down--;
            left++;
            right--;
        }
        if (left == right) {
            for (int i=up; i<=down; i++) {
                res.add(matrix[i][left]);
            }
        } else if (up == down) {
            for (int i=left; i<=right; i++) {
                res.add(matrix[up][i]);
            }
        }
        return res;
    }
}

