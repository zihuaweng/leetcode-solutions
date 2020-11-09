// https://leetcode.com/problems/rotate-image/
// http://javabypatel.blogspot.com/2016/11/rotate-matrix-by-90-degrees-inplace.html

class Solution {
    public void rotate(int[][] matrix) {
        int n = matrix.length;
        for (int i=0; i<n/2; i++) {
            for (int j=i; j<n-1-i; j++) {
                int temp=matrix[i][j];
                matrix[i][j]=matrix[n-1-j][i];
                matrix[n-1-j][i]=matrix[n-1-i][n-1-j];
                matrix[n-1-i][n-1-j]=matrix[j][n-1-i];
                matrix[j][n-1-i]=temp;
            }
        }
    }
}