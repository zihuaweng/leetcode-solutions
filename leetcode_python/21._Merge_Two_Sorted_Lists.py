# https://leetcode.com/problems/merge-two-sorted-lists/
# 设置一个新的head, 一个小技巧是随便设一个，最后返回head.next就可以不用重复写判断大小代码
# 两个指针在来那个链表上面走

# Time complexity: O(n+m)
# Space complexity: O(1)


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        temp = head

        while l1 is not None and l2 is not None:
            if l1.val > l2.val:
                temp.next = l2
                l2 = l2.next
            else:
                temp.next = l1
                l1 = l1.next
            temp = temp.next

        if l1 is not None:
            temp.next = l1
        else:
            temp.next = l2

        return head.next
