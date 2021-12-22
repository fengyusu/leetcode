
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList0(self, head: ListNode) -> ListNode:
        reverse_list = ListNode()
        while head:
            current_node = head
            head = head.next
            current_node.next = reverse_list.next
            reverse_list.next = current_node
        return reverse_list.next

    # double point
    def reverseList1(self, head: ListNode) -> ListNode:
        cur = None
        pre = head
        while pre:
            tmp = pre.next
            pre.next = cur
            cur,pre = pre,tmp
        return cur

    def reverseList2(self, head):
        if head == None or head.next == None:
            return head

        reverse = None
        current_node = head
        while current_node:
            next = current_node.next
            reverse, current_node.next = current_node, reverse
            current_node = next

        return reverse
