

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def arr_to_list(arr):
    n = len(arr)
    if n == 0:
        return None
    head = ListNode()
    cur = head
    for i in range(n):
        cur.next = ListNode(arr[i])
        cur = cur.next
    return head.next

def list_to_arr(head):
    arr = []
    while head:
        arr.append(head.val)
        head = head.next
    return arr

