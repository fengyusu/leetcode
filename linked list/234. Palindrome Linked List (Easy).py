

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode):
        dummy = ListNode()
        while head:
            tmp = head.next
            head.next = dummy.next
            dummy.next = head
            head = tmp
        return dummy.next

    def isPalindrome(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return True
        length = 0
        p = head
        while p:
            p = p.next
            length += 1
        mid = head
        for i in range((length+1) // 2):
            mid = mid.next
        mid = self.reverseList(mid)
        while mid:
            if head.val != mid.val:
                return False
            head = head.next
            mid = mid.next
        return True
