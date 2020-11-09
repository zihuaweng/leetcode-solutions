"""
https://leetcode.com/problems/all-oone-data-structure/discuss/91401/Python-O(1)-doubly-linked-list-and-dictionary

double linked list:

head. ---- freq1         ----    freq2           ------     freq3    --- tail
()       set(key1, key2)     set(key3, key4, key5)         set(key6)        ()

key2node dict:
key1 : node(freq1)
key3 : node(freq2)

inc: 
    1. get the node using key2node
        1. not in key2node: cur = head
        2. in key2node: get key2node[key], 
            del key from node
    2. add key to next node
        1. if next node not existing: add node to double linked list
            check if next freq = freq + 1
        2. add key to next node
        3. key2node[key] = next node
    3. delete cur node if len(node) == 0
        
dec:
    1. get the node using key2node
        1. not in key2node: return 
        2. in key2node: del key from node
        
    2. add key to prev node
        1. if prev node not existing: add node to double linked list
            check if prev freq = freq - 1
        2. add key to prev node
        3. key2node[key] = prev node
    3. if len(node) == 0: del cur node
        
max:
    1. get val of tail prev node
        1. return key if len() > 0
        2. return '' if len() == 0
        
max:
    1. get val of head next node
        1. return key if len() > 0
        2. return '' if len() == 0
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.keys = set()
        self.prev = None
        self.next = None
        
    def remove(self):  # this is so clever to remove itself
        self.prev.next = self.next
        self.next.prev = self.prev
        self.prev = None
        self.next = None
        
    def insert_after(self, new_node):
        temp = self.next
        self.next = new_node
        new_node.prev = self
        new_node.next = temp
        temp.prev = new_node

class AllOne:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = Node(0)  # freq == 0
        self.tail = Node(0)  # freq == 0
        self.head.next = self.tail
        self.tail.prev = self.head
        self.key2node = {}
        

    def inc(self, key: str) -> None:
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        """
        if key in self.key2node:
            cur_node = self.key2node[key]
            cur_node.keys.remove(key)
        else:
            cur_node = self.head
            
        cur_freq = cur_node.val
        if cur_freq + 1 != cur_node.next.val:
            new_node = Node(cur_freq+1)
            cur_node.insert_after(new_node)
        
        cur_node.next.keys.add(key)
        self.key2node[key] = cur_node.next
        
        if not cur_node.keys and cur_node.val != 0:
            cur_node.remove()
            

    def dec(self, key: str) -> None:
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        """
        if key not in self.key2node:
            return
        
        cur_node = self.key2node[key]
        cur_node.keys.remove(key)
        
        cur_freq = cur_node.val
        if cur_freq - 1 != cur_node.prev.val:
            new_node = Node(cur_freq - 1)
            cur_node.prev.insert_after(new_node)
            
        cur_node.prev.keys.add(key)
        self.key2node[key] = cur_node.prev
        
        if not cur_node.keys:
            cur_node.remove()
        

    def getMaxKey(self) -> str:
        """
        Returns one of the keys with maximal value.
        """
        cur_node = self.tail.prev
        if not cur_node.keys:
            return ''
        key = cur_node.keys.pop()
        cur_node.keys.add(key)
        return key
        

    def getMinKey(self) -> str:
        """
        Returns one of the keys with Minimal value.
        """
        cur_node = self.head.next
        if not cur_node.keys:
            return ''
        key = cur_node.keys.pop()
        cur_node.keys.add(key)
        return key


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()