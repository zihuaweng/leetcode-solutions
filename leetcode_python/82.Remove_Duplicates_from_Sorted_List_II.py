# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
# Time complexity: O(n)
# Space complexity: O(1)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        """
        dummy -> head -> head_next ->
          |        |      
         prev     cur
         
         check cur.val == cur.next.val, keep updating cur to cur.next
         else:
            prev = prev.next
            cur = cur.next
    
        """
        dummy = ListNode()
        dummy.next = head
        pre = dummy
        
        while head and head.next:
            if head.val == head.next.val:
                while head and head.next and head.val == head.next.val:
                    head = head.next
                    
                head = head.next
                pre.next = head
            
            else:
                pre = pre.next
                head = head.next
                
        return dummy.next
            