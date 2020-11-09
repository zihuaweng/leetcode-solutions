package com.leetcode;

// https://leetcode.com/problems/game-of-life/
// 289. Game of Life

class Solution {
    public void gameOfLife(int[][] board) {
        int m = board.length;
        int n = board[0].length;

        for (int i=0; i<m; i++) {
            for (int j=0; j<n; j++) {
                int lives = 0;
                for (int k=Math.max(0, i-1); k<Math.min(m, i+2); k++) {
                    for (int l=Math.max(0, j-1); l<Math.min(n, j+2); l++) {
                        lives += board[k][l] & 1;
                    }
                }
                if (lives == 3 || lives - board[i][j] == 3) {
                    board[i][j] += 2;
                }
            }
        }

        for (int i=0; i<m; i++) {
            for (int j=0; j<n; j++) {
                board[i][j] >>= 1;
            }
        }
    }
}