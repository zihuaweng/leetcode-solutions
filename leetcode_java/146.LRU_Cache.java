// https://leetcode.com/problems/lru-cache/

class LRUCache {

  private Map<Integer, Integer> cache;
  private final int capacity;

  public LRUCache(int capacity) {
    this.capacity = capacity;
    this.cache = new LinkedHashMap<>(capacity, 1.0f, true) {
      public boolean removeEldestEntry(Map.Entry eldest) {
        return cache.size() > capacity;
      }
    };
  }

  public int get(int key) {
    return cache.getOrDefault(key, -1);
  }

  public void put(int key, int value) {
    cache.put(key, value);
  }
}

/**
 * Your LRUCache object will be instantiated and called as such: LRUCache obj =
 * new LRUCache(capacity); int param_1 = obj.get(key); obj.put(key,value);
 */