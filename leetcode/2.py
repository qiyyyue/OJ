# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        def addTwoListNum(l1: ListNode, l2: ListNode, tmp_num: int) -> ListNode:
            if l1 == None and l2 == None:
                if tmp_num == 0:
                    return None
                else:
                    return ListNode(tmp_num)
            elif l1 == None:
                cur_val = l2.val + tmp_num
                cur_node = ListNode(cur_val % 10)
                next_node = addTwoListNum(None, l2.next, cur_val // 10)
                cur_node.next = next_node
                return cur_node
            elif l2 == None:
                cur_val = l1.val + tmp_num
                cur_node = ListNode(cur_val % 10)
                next_node = addTwoListNum(l1.next, None, cur_val // 10)
                cur_node.next = next_node
                return cur_node
            else:
                cur_val = l1.val + l2.val + tmp_num
                cur_node = ListNode(cur_val % 10)
                next_node = addTwoListNum(l1.next, l2.next, cur_val // 10)
                cur_node.next = next_node
                return cur_node

        return addTwoListNum(l1, l2, 0)