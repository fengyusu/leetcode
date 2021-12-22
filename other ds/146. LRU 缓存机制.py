class ListNode:
    def __init__(self, key = None, value = None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {}
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def move_node_to_tail(self, key):
        cur_node = self.hashmap[key]
        cur_node.prev.next = cur_node.next
        cur_node.next.prev = cur_node.prev
        self.tail.prev.next = cur_node
        cur_node.prev = self.tail.prev
        self.tail.prev = cur_node
        cur_node.next = self.tail

    def get(self, key: int) -> int:
        if key in self.hashmap.keys():
            self.move_node_to_tail(key)
            return self.hashmap[key].value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap.keys():
            self.hashmap[key].value = value
            self.move_node_to_tail(key)
        else:
            if len(self.hashmap) == self.capacity:
                del_key = self.head.next.key
                del_node = self.hashmap[del_key]
                self.hashmap.pop(del_key)
                self.head.next = del_node.next
                del_node.next.prev = self.head
                del(del_node)
            node = ListNode(key, value)
            node.prev = self.tail.prev
            node.next = self.tail
            self.tail.prev.next = node
            self.tail.prev = node
            self.hashmap[key] = node







