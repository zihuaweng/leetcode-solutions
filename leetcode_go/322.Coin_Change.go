// https://leetcode.com/problems/coin-change/

func coinChange(coins []int, amount int) int {
    dp := make([]int, amount+1)
    
    for i:=1; i<amount+1;i++ {
        dp[i] = amount+1
        for _, c := range coins {
            if i>=c && dp[i-c]+1 < dp[i] {
                dp[i] = dp[i-c]+1
            }
        }
    }
    
    if dp[amount] == amount+1 {
        return -1
    }
    return dp[amount]
}