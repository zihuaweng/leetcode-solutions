// https://leetcode.com/problems/container-with-most-water/submissions/

func maxArea(height []int) int {
	left, right, res := 0, len(height)-1, 0

	for left < right {
		w := right - left
		h := 0

		if height[left] <= height[right] {
			h = height[left]
			left++
		} else {
			h = height[right]
			right--
		}

		if w*h > res {
			res = w * h
		}
	}

	return res
}