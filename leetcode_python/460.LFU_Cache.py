"""

double linked list:

head. ---- freq1         ----    freq2           ------     freq3    --- tail
()  (bucket 1:key1, key2)    (b2: key3, key4, key5)      (b3: key6)        ()


for each bucket above is double linked list:

head  -  key1 - key2 - key3 - key4 - key5  - tail

key2node dict:
key1 : node(freq1)
key3 : node(freq2)

key2bucketnode:
key1 : node(b1 key1 node)
key3 : node(b2 key3 node)

get:
    1. find key in key2node
        1. not in: return -1
        2. in : 
            1. get the value
            2. cur_node = key2node[key]
                delete key from cur_node
    2. update get next_node
        1.check if freq + 1 == next_node.val
            1. not: create next_node
    2. add key to next_node
        1. if key in bucket, check key in key2bucketnode
            del key2bucketnode[key]
        2. add a new node to the end of next_node
        3. key2bucketnode[key] = new node
        4. key2node[key] = next_node
        
put:
    1. find key in key2node
        1. not in: cur_node = head
        2. in : cur_node = key2node[key]
            delete key from cur_node
    2. get next_node
        1.check if freq + 1 == next_node.val
            1. not: create next_node
    2. add key to next_node
        1. if key in bucket, check key in key2bucketnode
            del key2bucketnode[key]
        2. add a new node to the end of next_node
        3. key2bucketnode[key] = new node
        4. key2node[key] = next_node
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.


class LFUCache:

    def __init__(self, capacity: int):
        

    def get(self, key: int) -> int:
        

    def put(self, key: int, value: int) -> None:
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)