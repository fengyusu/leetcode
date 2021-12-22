from utils import arr_to_list,list_to_arr


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def list_lens(self,list_node):
        lens = 0
        while list_node:
            list_node = list_node.next
            lens += 1
        return lens

    def reverse_list(self, head, k):
        if head == None or head.next == None:
            return head,head,head.next

        reverse = None
        current_node = head
        while k:
            k -= 1
            next = current_node.next
            reverse, current_node.next = current_node, reverse
            current_node = next
        return reverse, head, current_node


    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        lens = self.list_lens(head)
        groups = lens // k

        current_list = head
        reverse = ListNode()
        last = reverse
        for i in range(groups):
            last.next, last, current_list= self.reverse_list(current_list, k)
        last.next = current_list

        return reverse.next



if __name__ == '__main__':
    arr = [1,2,3,4,5,6]
    list_node = arr_to_list(arr)
    solution = Solution()
    result = solution.reverseKGroup(list_node, 7)
    print(list_to_arr(result))

