// https://leetcode.com/problems/group-anagrams/

class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        if (strs.length == 0 || strs == null) {
            return new ArrayList<>();
        }
        Map<String, List<String>> res = new HashMap<>();
        for (String s: strs) {
            int[] ca = new int[26];
            for (char c: s.toCharArray()) {
                ca[c-'a']++;
            }
            String key = Arrays.toString(ca);
            if (!res.containsKey(key)) {
                res.put(key, new ArrayList<>());
            }
            res.get(key).add(s);
        }
        return new ArrayList<>(res.values());
    }
}