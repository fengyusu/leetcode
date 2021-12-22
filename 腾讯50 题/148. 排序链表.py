
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def merge(self, l1, l2):
        head = ListNode()
        prev = head
        while l1 and l2:
            if l1.val < l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next
        if l1:
            prev.next = l1
        if l2:
            prev.next =l2
        return head.next

    def sortList(self, head, tail):
        if not head:
            return head
        if head.next == tail:
            head.next = None
            return head
        slow = fast = head
        while fast != tail:
            slow = slow.next
            fast = fast.next
            if fast != tail:
                fast = fast.next
        mid = slow
        return self.merge(self.sortList(head, mid), self.sortList(mid, tail))

    def sortList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head

        return self.sortList(head,None)
