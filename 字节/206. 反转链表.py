# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        dummy = ListNode()
        while head:
            tmp = head
            head.next = dummy.next
            dummy.next = head
            head = tmp
        return dummy.next