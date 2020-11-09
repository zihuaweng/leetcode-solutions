# https://leetcode.com/problems/design-linked-list/

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class MyLinkedList(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.length = 0
        self.head = None

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if index < 0 or index >= self.length:
            return -1
        if self.head is None:
            return -1
        temp = self.head
        while index > 0:
            temp = temp.next
            index -= 1
        return temp.val

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: None
        """
        self.addAtIndex(0, val)

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: None
        """
        self.addAtIndex(self.length, val)

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: None
        """
        # 这里的index小于0也可以插入到头部
        if index > self.length:
            return
        node = ListNode(val)
        if index <= 0:
            node.next = self.head
            self.head = node
        else:
            temp = self.head
            while index > 1:
                temp = temp.next
                index -= 1
            node.next = temp.next
            temp.next = node
        self.length += 1

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: None
        """
        # 这里的index小于0无返回
        if index < 0 or index >= self.length:
            return

        temp = self.head
        if index == 0:
            self.head = temp.next
        else:
            while index > 1:
                temp = temp.next
                index -= 1

            temp.next = temp.next.next
        self.length -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
