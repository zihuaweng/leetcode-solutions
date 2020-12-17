// https://leetcode.com/problems/lru-cache/

class LRUCache {
 private:
  unordered_map<int, int> key2val;
  list<int> nodes;
  int cap;
  unordered_map<int, list<int>::iterator> key2node;

 public:
  LRUCache(int capacity) { cap = capacity; }

  int get(int key) {
    if (key2node.find(key) == key2node.end()) {
      return -1;
    }
    auto node = key2node[key];
    nodes.erase(node);
    nodes.push_back(key);
    key2node[key] = --nodes.end();
    return key2val[key];
  }

  void put(int key, int value) {
    if (get(key) != -1) {
      key2val[key] = value;
      return;
    }

    if (key2node.size() == cap) {
      auto to_delete = nodes.begin();
      key2val.erase(*to_delete);
      key2node.erase(*to_delete);
      nodes.erase(to_delete);
    }

    nodes.push_back(key);
    key2val[key] = value;
    key2node[key] = --nodes.end();
  }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */