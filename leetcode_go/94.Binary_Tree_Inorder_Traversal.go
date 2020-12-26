// https://leetcode.com/problems/binary-tree-inorder-traversal/

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func inorderTraversal(root *TreeNode) []int {
    stack := make([]*TreeNode, 0)
    res := make([]int, 0)
    
    for root != nil || len(stack) != 0 {
        for root != nil {
            stack = append(stack, root)
            root = root.Left
        }
        cur := stack[len(stack)-1]
        stack = stack[:len(stack)-1]
        res = append(res, cur.Val)
        root = cur.Right
    }
    
    return res
}