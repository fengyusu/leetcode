class ListNode:
    def __init__(self, key = None, value = None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.head = ListNode()
        self.tail = ListNode()
        self.tail.prev = self.head
        self.head.next = self.tail
        self.capacity = capacity
        self.hash = dict()


    def get(self, key: int) -> int:
        if key not in self.hash:
            return -1
        cur_node = self.hash[key]
        cur_node.prev.next = cur_node.next
        cur_node.next.prev = cur_node.prev
        cur_node.next = self.head.next
        self.head.next.prev = cur_node
        self.head.next = cur_node
        cur_node.prev = self.head
        return cur_node.value

    def put(self, key: int, value: int) -> None:
        if key in self.hash:
            self.hash[key].value = value
            self.get(key)
        else:
            cur_node = ListNode(key, value)
            cur_node.next = self.head.next
            self.head.next.prev = cur_node
            self.head.next = cur_node
            cur_node.prev = self.head
            self.hash[key] = cur_node
            if len(self.hash) > self.capacity:
                del_node = self.tail.prev
                del_node.prev.next = del_node.next
                del_node.next.prev = del_node.prev
                self.hash.pop(del_node.key)
                del(del_node)




# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)