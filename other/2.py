# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def nodeLens(self, l:ListNode) -> int:
        lens  = 1
        while l.next != None:
            l = l.next
            lens += 1
        return lens

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        lens1 = self.nodeLens(l1)
        lens2 = self.nodeLens(l2)
        if lens1 < lens2:
            l1,l2 = l2,l1
            lens1,lens2 = lens2,lens1

        sum_node = ListNode()
        last_node = sum_node
        overflow = 0

        for i in range(lens1):
            new_node = ListNode(0)
            last_node.next = new_node
            last_node = new_node

            if(i < lens2):
                total_val = l1.val + l2.val + overflow
                new_node.val = total_val % 10
                overflow = total_val // 10
                l1 = l1.next
                l2 = l2.next
            else:
                total_val = l1.val + overflow
                new_node.val = total_val % 10
                overflow = total_val // 10
                l1 = l1.next

        if overflow:
            new_node = ListNode(1)
            last_node.next = new_node

        sum_node = sum_node.next

        return sum_node

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
