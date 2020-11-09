# https://leetcode.com/problems/intersection-of-two-linked-lists/
# method 1
# 两个链表如果有交叉的话，后面重合的部分是一样长度的。
# 所以首先遍历到两个链表一样长度的地方，然后两个链表同时前向遍历
# 判断是否有一样，一样就停止返回

# method 2
# https://leetcode.com/problems/intersection-of-two-linked-lists/discuss/49798/Concise-python-code-with-comments
# 两个指针拼接,如果有一样的话会访问到同一个节点，同时消除链表长度不同的问题

# Time complexity: O(n+m)
# Space complexity: O(1)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # method 1
        len_a = 0
        len_b = 0
        l_a = headA
        l_b = headB
        while l_a is not None:
            len_a += 1
            l_a = l_a.next
        while l_b is not None:
            len_b += 1
            l_b = l_b.next
        # 走到两个链表一样的地方
        # 也可以写一个判断，len_a, len_b
        while len_a > len_b:
            len_a -= 1
            headA = headA.next
        while len_b > len_a:
            len_b -= 1
            headB = headB.next

        # 找到一样长的地方有没有相同的点
        # 这里注意不能用while headA.val !== headB.val
        # 因为有可能两个链表没有重合的部分，headA和headB都会为None，这样就没有val属性，所以会报错。
        while headA is not headB:
            headA = headA.next
            headB = headB.next

        return headA

        # # method 2
        # if not headA or not headB:
        #     return None
        #
        # p_a = headA
        # p_b = headB
        #
        # while p_a is not p_b:
        #     p_a = headB if not p_a else p_a.next
        #     p_b = headA if not p_b else p_b.next
        #
        # return p_a
