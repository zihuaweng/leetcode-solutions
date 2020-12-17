// https://leetcode.com/problems/lru-cache/

class Node {
  int key;
  int val;
  Node prev;
  Node next;

  public Node(int key, int val) {
    this.key = key;
    this.val = val;
  }

  public Node() {
    this.key = 0;
    this.val = 0;
  }

  public void deleteNode() {
    prev.next = next;
    next.prev = prev;
  }
}

class LRUCache {

  private int capacity;
  private Node head;
  private Node tail;
  private Map<Integer, Node> cache;

  public LRUCache(int capacity) {
    this.capacity = capacity;
    this.cache = new HashMap<>();
    this.head = new Node();
    this.tail = new Node();
    head.next = tail;
    tail.prev = head;
  }

  public int get(int key) {
    Node node = cache.get(key);
    if (node == null) {
      return -1;
    } else {
      node.deleteNode();
      add(node);
    }

    return node.val;
  }

  public void put(int key, int value) {
    Node node = cache.get(key);
    if (node == null) {
      Node newNode = new Node(key, value);
      cache.put(key, newNode);
      add(newNode);

      if (cache.size() > capacity) {
        Node toDelete = head.next;
        toDelete.deleteNode();
        cache.remove(toDelete.key);
      }
    } else {
      node.deleteNode();
      node.val = value;
      add(node);
    }
  }

  public void add(Node node) {
    Node prev_tail = tail.prev;
    prev_tail.next = node;
    node.prev = prev_tail;
    node.next = tail;
    tail.prev = node;
  }
}

/**
 * Your LRUCache object will be instantiated and called as such: LRUCache obj =
 * new LRUCache(capacity); int param_1 = obj.get(key); obj.put(key,value);
 */