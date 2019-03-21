#coding: utf8
'''
链表环
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None:
            return False
        elif head.next == None:
            return False

        p = head
        q = head.next

        while p and q:
            if p == q:
                return True
            if p.next:
                p = p.next
            else:
                break
            if q.next and q.next.next:
                q = q.next.next
            else:
                break
        return False