
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        count = 0
        dummy = ListNode(0)
        dummy.next = head
        p1 = dummy
        p2 = dummy

        while p1 != None:
            p1 = p1.next
            count += 1
            if count > n+1:
                p2 = p2.next
        del_node = p2.next
        p2.next = p2.next.next
        del(del_node)

        return dummy.next






