// https://leetcode.com/problems/median-of-two-sorted-arrays/submissions/
// https://www.youtube.com/watch?v=ScCg9v921ns

class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        if (nums1.length > nums2.length) {
            return findMedianSortedArrays(nums2, nums1);
        }
        int len1 = nums1.length;
        int len2 = nums2.length;
        int len = len1 + len2;
        if (len1 == 0) {
            return (double) (nums2[len2/2] + nums2[(len2-1)/2]) / 2;
        }
        int left = 0;
        int right = len1;
        while (left <= right) {
            int mid1 = left + (right-left) / 2;   // nums1 左边元素个数
            int mid2 = len / 2 - mid1;        // nums2 左边元素个数
            double L1 = (mid1 == 0) ? Integer.MIN_VALUE : nums1[mid1-1];
            double L2 = (mid2 == 0) ? Integer.MIN_VALUE : nums2[mid2-1];
            double R1 = (mid1 == len1) ? Integer.MAX_VALUE : nums1[mid1];
            double R2 = (mid2 == len2) ? Integer.MAX_VALUE : nums2[mid2];
            if (L1 > R2) {
                right = mid1 - 1;
            } else if (L2 > R1) {
                left = mid1 + 1;
            } else {
                if (len % 2 == 0) {
                    return (Math.max(L1, L2) + Math.min(R1, R2)) / 2;
                } else {
                    return Math.min(R1, R2);
                }
            }
        }
        return -1;
    }
}