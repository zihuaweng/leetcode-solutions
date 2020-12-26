// https://leetcode.com/problems/clone-graph/

/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/

class Solution {
 public:
  Node* cloneGraph(Node* node) {
    if (node == NULL) return NULL;
    unordered_map<Node*, Node*> Map;
    queue<Node*> q;
    q.push(node);
    Map[node] =
        new Node(node->val);  // create a new object and return its pointer

    while (!q.empty()) {
      Node* root = q.front();
      q.pop();
      for (int i = 0; i < root->neighbors.size(); i++) {
        if (Map.find(root->neighbors[i]) == Map.end()) {
          Node* new_node = new Node(root->neighbors[i]->val);
          Map[root->neighbors[i]] = new_node;
          Map[root]->neighbors.push_back(new_node);
          q.push(root->neighbors[i]);
        } else {
          Map[root]->neighbors.push_back(Map[root->neighbors[i]]);
        }
      }
    }

    return Map[node];
  }
};