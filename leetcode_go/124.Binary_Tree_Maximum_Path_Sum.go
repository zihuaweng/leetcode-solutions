import "math"

// https://leetcode.com/problems/binary-tree-maximum-path-sum/

func maxPathSum(root *TreeNode) int {
	if root == nil {
		return 0
	}

	maxVal := math.MinInt32

	dfs(root, &maxVal)
	return maxVal
}

func dfs(node *TreeNode, val *int) int {
	if node == nil {
		return 0
	}

	left := dfs(node.Left, val)
	right := dfs(node.Right, val)
	*val = max(*val, node.Val+left+right)

	return max(0, node.Val+max(left, right))
}

func max(a int, b int) int {
	if a > b {
		return a
	}
	return b
}