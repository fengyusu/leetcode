import math
from typing import List

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

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None

        cur_list_len = len(lists)
        cur_list = lists
        while cur_list_len > 1:
            new_list = []
            for i in range(math.ceil(cur_list_len / 2)):
                head1_index = i * 2
                head2_index = i * 2 + 1
                new_list.append(self.merge(cur_list[head1_index], cur_list[head2_index] if head2_index < cur_list_len else None)[0])

            cur_list = new_list
            cur_list_len = len(cur_list)

        return cur_list[0]
