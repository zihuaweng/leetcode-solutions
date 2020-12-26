// https://leetcode.com/problems/clone-graph/

/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> neighbors;
    public Node() {
        val = 0;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val) {
        val = _val;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val, ArrayList<Node> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
}
*/

class Solution {
  public Node cloneGraph(Node node) {
    if (node == null) {
      return null;
    }

    Map<Node, Node> map = new HashMap<>();
    map.put(node, new Node(node.val));
    Queue<Node> queue = new LinkedList<>();
    queue.offer(node);

    while (!queue.isEmpty()) {
      Node root = queue.poll();
      for (Node child : root.neighbors) {
        if (!map.containsKey(child)) {
          Node newChild = new Node(child.val);
          map.put(child, newChild);
          map.get(root).neighbors.add(newChild);
          queue.offer(child);
        } else {
          map.get(root).neighbors.add(map.get(child));
        }
      }
    }

    return map.get(node);
  }
}