#!/usr/bin/env python3
# coding: utf-8

# https://leetcode.com/problems/lru-cache/
# 使用双向链表

# 另一种方法使用OrderedDict


# Time complexity: O()
# Space complexity: O()

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.pre = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.ele = dict()
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.pre = self.head

    def get(self, key: int) -> int:
        if key in self.ele:
            node = self.ele[key]
            self._remove(node)
            self._add(node)
            return node.val

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.ele:
            self._remove(self.ele[key])
        elif len(self.ele) == self.capacity:
            self._remove(self.head.next)
        node = Node(key, value)
        self._add(node)

    def _add(self, node):
        last = self.tail.pre
        last.next = node
        node.pre = last
        node.next = self.tail
        self.tail.pre = node
        self.ele[node.key] = node

    def _remove(self, node):
        pre = node.pre
        pre.next = node.next
        node.next.pre = pre
        del self.ele[node.key]

    def _print_node(self):
        head = self.head
        res = []
        while head is not None:
            res.append(head.key)
            head = head.next

        print(res)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)




class Node:
    def __init__(self, key=None, val=None, prev=None, n=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = n
        
    def delete(self):
        self.prev.next = self.next
        self.next.prev = self.prev
        self.preb = None
        self.next = None
        

class LRUCache:
    """
    nodes: double linkedlist: head - node - tail
    key2node: dict, find linkedlist node using key
    
    get: 
        - find if key in key2node
            - yes: 
                - del key from nodes
                - add key to the end of nodes
                - update key2node
            - no: return -1
        
    put
        - find if key in key2node
            - yes: 
                - del key from nodes
                - add key to the end of nodes
                - update key2node
                - update node val
            - no:
                - check if oversize
                    - yes, delete first one
                - create node
                - add key to the end of nodes
                - add node to key2node
    
    """

    def __init__(self, capacity: int):
        self.size = capacity
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.d = {}
        

    def get(self, key: int) -> int:
        # print(self.d.keys())
        if key in self.d:
            node = self.d[key]
            node.delete()
            self._add(node)
            return node.val
        else:
            return -1
            

    def put(self, key: int, value: int) -> None:
        # print(self.d.keys())
        if key in self.d:
            node = self.d[key]
            node.delete()
        else:
            if len(self.d) == self.size:
                first = self.head.next
                first.delete()
                del self.d[first.key]
        
        node = Node(key, value)
        self._add(node)
        
    
    def _add(self, node):
        last = self.tail.prev
        last.next = node
        node.prev = last
        node.next = self.tail
        self.tail.prev = node
        self.d[node.key] = node
