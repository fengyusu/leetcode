

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def merge(self, head1, head2):
        dummy = ListNode()
        tmp = dummy
        while head1 and head2:
            if head1.val > head2.val:
                tmp.next = head2
                head2 = head2.next
            else:
                tmp.next = head1
                head1 = head1.next
            tmp = tmp.next
        if head1:
            tmp.next = head1
        if head2:
            tmp.next = head2
        while tmp.next:
            tmp = tmp.next
        return dummy.next, tmp



    def sortList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        dummy = ListNode(0,head)
        length = 0
        while head:
            length += 1
            head = head.next
        sub_length = 1
        print(length)
        while sub_length < length:
            print(sub_length)
            prev = dummy
            cur = dummy.next
            while cur:
                head1 = cur
                for i in range(sub_length-1):
                    if cur and cur.next:
                        cur = cur.next
                    else:
                        break
                if cur:
                    tmp = cur.next
                    cur.next = None
                    cur = tmp

                head2 = cur
                for i in range(sub_length-1):
                    if cur and cur.next:
                        cur = cur.next
                    else:
                        break
                if cur:
                    tmp = cur.next
                    cur.next = None
                    cur = tmp

                m_head, m_tail = self.merge(head1, head2)
                prev.next = m_head
                prev = m_tail

            sub_length *= 2

        return dummy.next


