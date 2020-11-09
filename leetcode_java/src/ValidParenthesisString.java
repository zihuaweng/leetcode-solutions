// https://leetcode.com/problems/valid-parenthesis-string/
// https://leetcode.com/problems/valid-parenthesis-string/discuss/107577/Short-Java-O(n)-time-O(1)-space-one-pass

class Solution {
    public boolean checkValidString(String s) {
        int low = 0;
        int hight = 0;
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == '(') {
                low++;
                hight++;
            } else if (c == ')') {
                if (low > 0) {
                    low --;
                }
                hight--;
            } else {
                if (low > 0) {
                    low --;
                }
                hight++;
            }
            if (hight < 0)
                return false;
        }
        return low == 0;
    }
}