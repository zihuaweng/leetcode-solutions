"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Codec:
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        pre_order = []
        
        def dfs(root):
            if not root:
                return None
            pre_order.append(str(root.val))
            pre_order.append(str(len(root.children)))
            for c in root.children:
                dfs(c)
                
        dfs(root)
        return ','.join(pre_order)
	
    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        if not data:
            return None
        
        queue = collections.deque(data.split(','))
        
        def dfs():
            if not queue:
                return None
            val = int(queue.popleft())
            count = int(queue.popleft())
            node = Node(val, [])
            for _ in range(count):
                node.children.append(dfs())
                
            return node
        
        return dfs()
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))