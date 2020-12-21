// https://leetcode.com/problems/coin-change/

class Solution {
 public:
  int coinChange(vector<int>& coins, int amount) {
    vector<int> dp(amount + 1, amount + 1);  // (size, default_value)
    dp[0] = 0;

    for (int i = 1; i < amount + 1; i++) {
      for (auto c : coins) {
        if (i >= c) {
          dp[i] = min(dp[i], dp[i - c] + 1);
        }
      }
    }

    return dp[amount] == amount + 1 ? -1 : dp[amount];
  }
};