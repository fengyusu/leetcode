
class ListNode:
    def __init__(self, val=None, next=None, prev=None, key=None):
        self.val = val
        self.next = next
        self.prev = prev
        self.key = key



class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = ListNode()
        self.rear = None
        self.map = {}

    def update_node_to_head(self, key):
        if self.head.next != self.map[key]:
            cur_node = self.map[key]

            cur_node.prev.next = cur_node.next
            if cur_node.next is None:
                self.rear == cur_node.prev
            else:
                cur_node.next.prev = cur_node.prev

            tmp = self.head.next
            self.head.next = cur_node
            cur_node.next = tmp
            # cur_node.prev = self.head
            cur_node.prev = None
            tmp.prev = cur_node

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        self.update_node_to_head(key)
        return self.map[key].val



    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.map[key].val = value
            self.update_node_to_head(key)
        else:
            if len(self.map) >= self.capacity:
                del_key = self.rear.key
                del_node = self.rear
                if del_node is not None:
                    self.rear = self.rear.prev
                    del del_node
                    del self.map[del_key]
            cur_node = ListNode(val=value, key=key)
            self.map[key] = cur_node

            tmp = self.head.next
            self.head.next = cur_node
            cur_node.next = tmp
            cur_node.prev = None
            if tmp is None:
                self.rear = cur_node
            else:
                tmp.prev = cur_node







# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)