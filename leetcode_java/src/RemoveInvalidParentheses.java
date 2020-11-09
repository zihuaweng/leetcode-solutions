//https://leetcode.com/problems/remove-invalid-parentheses/

package com.leetcode;

import java.util.*;

class Solution {

    public List<String> removeInvalidParentheses(String s) {
        int numToRemove = valid(s);
        Set<String> check = new HashSet<>();
        check.add(s);

        for (int i=0; i<numToRemove; i++) {

            Set<String> temp = new HashSet<>();
            for (String ele: check) {
                // String ele = check.poll();
                for (int j=0; j<ele.length(); j++) {
                    if (ele.charAt(j) == '(' || ele.charAt(j) == ')') {
                        temp.add(ele.substring(0, j) + ele.substring(j+1));
                    }
                }
                check = temp;
            }
        }
        List<String> ans = new ArrayList<>();
        for (String i: check) {
            if (valid(i) == 0) {
                ans.add(i);
            }
        }
        return ans;
    }

    private int valid(String ele) {
        Stack<Character> stack = new Stack<>();
        for (int i=0; i<ele.length(); i++) {
            char word = ele.charAt(i);
            if (!stack.empty() && stack.lastElement() == '(' && word == ')') {
                stack.pop();
            }
            else if (word == ')' || word == '(') {
                stack.push(word);
            }
        }
        return stack.size();
    }
}
