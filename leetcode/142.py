#coding: utf8

'''
circle of link_list
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        hash_dict = []

        while head:
            if head in hash_dict:
                return head
            else:
                hash_dict.append(head)
            head = head.next
        return None