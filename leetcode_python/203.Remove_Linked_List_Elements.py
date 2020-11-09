# https://leetcode.com/problems/remove-linked-list-elements/
# Time complexity: O(n)
# Space complexity: O(1) # 只是复制了一个ListNode

# 删除链表（1）删除当前元素的下一个元素：tmp.next = tmp.next.next
# 删除链表（2）删除当前元素：tmp.val = tmp.next.val; tmp.next = tmp.next.next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        # 先将前面满足删除条件的元素全部删除掉
        while head and head.val == val:
            head = head.next

        cur = head

        while cur and cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next

        return head


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        res = ListNode(0)
        res.next = head
        p = res
        while p and p.next:
            while p.next and p.next.val == val:
                p.next = p.next.next
            p = p.next

        return res.next
