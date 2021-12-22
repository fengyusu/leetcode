
class TrieNode:
    def __init__(self):
        self.is_val = False
        self.child_node = dict()

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        temp = self.root
        for s in word:
            if s not in temp.child_node:
                temp.child_node[s] = TrieNode()
            temp = temp.child_node[s]
        temp.is_val = True


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        temp = self.root
        for s in word:
            if temp is None or s not in temp.child_node:
                return False
            temp = temp.child_node[s]
        return temp.is_val if temp else False



    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        temp = self.root
        for s in prefix:
            if temp is None or s not in temp.child_node:
                return False
            temp = temp.child_node[s]
        return True



# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert("word")
obj.insert("world")
obj.insert("w2orld")
print(obj.search("word"))
print(obj.search("world"))
print(obj.search("world3"))
print(obj.startsWith("w32"))
print(obj.startsWith("wor"))