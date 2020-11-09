package com.leetcode;

// 297. Serialize and Deserialize Binary Tree
// https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

import javax.swing.tree.TreeNode;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.LinkedList;

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Codec {

    private ArrayList<String> treeList = new ArrayList<>();
    private static final String empty = "#";

    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        buildString(root);
        return String.join(",", treeList);
    }

    private void buildString(TreeNode node) {
        if (node == null) {
            treeList.add(empty);
        } else {
            treeList.add(Integer.toString(node.val));
            buildString(node.left);
            buildString(node.right);
        }
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        LinkedList<String> vals = new LinkedList<>(Arrays.asList(data.split(",")));
        TreeNode root = buildTree(vals);
        return root;
    }

    private TreeNode buildTree(LinkedList<String> vals) {
        if (vals == null) {
            return null;
        }
        String val = vals.remove();
        if (val.equals(empty)) {
            return null;
        }
        TreeNode node = new TreeNode(Integer.parseInt(val));
        node.left = buildTree(vals);
        node.right = buildTree(vals);
        return node;
    }
}

// Your Codec object will be instantiated and called as such:
// Codec codec = new Codec();
// codec.deserialize(codec.serialize(root));
