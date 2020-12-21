// https://leetcode.com/problems/jump-game-ii/

func jump(nums []int) int {
    start, end, step := 0,0,0
    if len(nums) == 1 {
        return step
    }
    
    for start <= end {
        new_end := 0
        for i:=start;i<=end;i++ {
            if nums[i]+i > new_end {
                new_end = nums[i]+i
            }
            if new_end >= len(nums)-1 {
                return step +1
            }
        }
        step++
        start = end+1
        end = new_end
    }
    return -1;
}