// https: // leetcode.com/problems/longest-valid-parentheses/

class Solution {
 public:
  int longestValidParentheses(string s) {
    stack<int> cache;
    int res = 0;

    for (int i = 0; i < s.size(); i++) {
      if (s[i] == '(') {
        cache.push(i);
      } else {
        if (!cache.empty() && s[cache.top()] == '(') {
          cache.pop();
          int left = cache.empty() ? -1 : cache.top();
          res = max(res, i - left);
        } else {
          cache.push(i);
        }
      }
    }

    return res;
  }
};