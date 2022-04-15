
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        dummy = ListNode()
        dummy.next = None
        while head:
            tmp = head.next
            head.next = dummy.next
            dummy.next = head
            head = tmp
        return dummy.next
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        overflow = 0
        l1 = self.reverseList(l1)
        l2 = self.reverseList(l2)
        dummy = ListNode()
        p = dummy
        while l1 or l2:
            cur_sum = overflow
            if l1:
                cur_sum += l1.val
                l1 = l1.next
            if l2:
                cur_sum += l2.val
                l2 = l2.next
            p.next = ListNode(val=cur_sum%10)
            p = p.next
            overflow = cur_sum // 10
        if overflow:
            p.next = ListNode(val=1)
        return self.reverseList(dummy.next)
