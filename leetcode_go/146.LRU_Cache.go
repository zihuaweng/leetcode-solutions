// https://leetcode.com/problems/lru-cache/

import "container/list"

type LRUCache struct {
	key2node map[int]*list.Element
	key2val  map[int]int
	nodes    *list.List
	capacity int
}

func Constructor(capacity int) LRUCache {
	return LRUCache{
		capacity: capacity,
		nodes:    list.New(),
		key2node: make(map[int]*list.Element, capacity),
		key2val:  make(map[int]int),
	}
}

func (this *LRUCache) Get(key int) int {
	if node, ok := this.key2node[key]; !ok {
		return -1
	} else {
		val := this.key2val[key]
		this.nodes.MoveToBack(node)
		return val
	}
}

func (this *LRUCache) Put(key int, value int) {
	if this.Get(key) != -1 {
		this.key2val[key] = value
		return
	} else {
		if len(this.key2node) == this.capacity {
			toDelete := this.nodes.Front()
			this.nodes.Remove(toDelete)
			delete(this.key2node, toDelete.Value.(int)) //Type assertions
			delete(this.key2val, toDelete.Value.(int))  //Type assertions
		}

		this.nodes.PushBack(key)
		this.key2node[key] = this.nodes.Back()
		this.key2val[key] = value
	}
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * obj := Constructor(capacity);
 * param_1 := obj.Get(key);
 * obj.Put(key,value);
 */