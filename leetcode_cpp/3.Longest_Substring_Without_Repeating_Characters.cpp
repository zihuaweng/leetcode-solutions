// https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution {
 public:
  int lengthOfLongestSubstring(string s) {
    unordered_map<int, int> map;

    int i = 0;
    int res = 0;
    for (int j = 0; j < s.size(); j++) {
      if (map.find(s[j]) != map.end()) {
        i = max(i, map[s[j]] + 1);
      }
      map[s[j]] = j;
      res = max(res, j - i + 1);
    }
    return res;
  }
};