// https: // leetcode.com/problems/longest-valid-parentheses/

func longestValidParentheses(s string) int {
    stack := []int{}
    res := 0
    
    for i, c := range s {
        if c == '(' {
            stack = append(stack, i)
        } else {
            if len(stack) != 0 && s[stack[len(stack)-1]] == '('{
                stack = stack[:len(stack)-1]
                left := -1
                if len(stack) > 0 {
                    left = stack[len(stack)-1]
                }
                if res < i-left {
                    res = i-left
                }
                
            } else {
                stack = append(stack, i)
            }
        }
    }
    return res
}