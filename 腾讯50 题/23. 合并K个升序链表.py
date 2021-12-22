
# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        n = len(lists)
        if n == 0:
            return None
        if n == 1:
            return lists[0]
        mid = n // 2
        l_list = self.mergeKLists(lists[0:mid])
        r_list = self.mergeKLists(lists[mid:])
        new_list = ListNode()
        prev = new_list
        while l_list and r_list:
            if l_list.val <= r_list.val:
                prev.next = l_list
                l_list = l_list.next
            else:
                prev.next = r_list
                r_list = r_list.next
            prev = prev.next
        if l_list:
            prev.next = l_list
        if r_list:
            prev.next = r_list
        return new_list.next

