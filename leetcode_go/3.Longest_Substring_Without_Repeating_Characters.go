// https://leetcode.com/problems/longest-substring-without-repeating-characters/

func lengthOfLongestSubstring(s string) int {
	i, res := 0, 0
	m := map[string]int{}

	for j := 0; j < len(s); j++ {
		if index, ok := m[string(s[j])]; ok {
			i = max(i, index+1)
		}
		m[string(s[j])] = j
		res = max(res, j-i+1)
	}
	return res
}

func max(a int, b int) int {
	if a >= b {
		return a
	}
	return b
}