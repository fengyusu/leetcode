
class TrieNode:
    def __init__(self):
        self.child = {}
        self.val = 0
        self.prefix_sum = 0

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()


    def insert(self, word: str, val, prev_val) -> None:
        """
        Inserts a word into the trie.
        """
        cur_level = self.root
        for c in word:
            if c not in cur_level.child:
                cur_level.child[c] = TrieNode()
            cur_level = cur_level.child[c]
            cur_level.prefix_sum -= prev_val
            cur_level.prefix_sum += val

        cur_level.val = val




    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cur_level = self.root
        for c in prefix:
            if c not in cur_level.child:
                return 0
            cur_level = cur_level.child[c]
        return cur_level.prefix_sum


class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = {}
        self.trie = Trie()


    def insert(self, key: str, val: int) -> None:
        prev_val = 0
        if key in self.map:
            prev_val = self.map[key]
        self.map[key] = val
        self.trie.insert(key, val, prev_val)




    def sum(self, prefix: str) -> int:
        return self.trie.startsWith(prefix)



# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)