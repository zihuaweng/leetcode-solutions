// https://leetcode.com/problems/sliding-window-maximum/

func maxSlidingWindow(nums []int, k int) []int {
    deque := make([]int, 0, k)
    res := make([]int, 0, len(nums)-k+1)
    
    for i, value := range nums {
        if len(deque) > 0 && deque[0] <= i - k {
            deque = deque[1:]
        }
        
        for len(deque) > 0 && nums[deque[len(deque)-1]] <= value {
            deque = deque[:len(deque)-1]
        }
        
        deque = append(deque, i)
        
        if i >= k - 1 {
            res = append(res, nums[deque[0]])
        } 
    }
    
    return res
}