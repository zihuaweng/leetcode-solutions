// https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution {
  public int lengthOfLongestSubstring(String s) {
    HashMap<Character, Integer> map = new HashMap<>();

    int i = 0;
    int res = 0;

    for (int j = 0; j < s.length(); j++) {
      if (map.containsKey(s.charAt(j))) {
        i = Math.max(i, map.get(s.charAt(j)) + 1);
      }
      map.put(s.charAt(j), j);
      res = Math.max(res, j - i + 1);
    }

    return res;
  }
}