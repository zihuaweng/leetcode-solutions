// https: // leetcode.com/problems/longest-valid-parentheses/

class Solution {
  public int longestValidParentheses(String s) {
    int res = 0;
    Stack<Integer> stack = new Stack<>();

    for (int i = 0; i < s.length(); i++) {
      if (s.charAt(i) == ')') {
        if (!stack.isEmpty() && s.charAt(stack.peek()) == '(') {
          stack.pop();
          int left = stack.isEmpty() ? -1 : stack.peek();
          res = Math.max(res, i - left);
        } else {
          stack.push(i);
        }
      } else {
        stack.push(i);
      }
    }

    return res;
  }
}