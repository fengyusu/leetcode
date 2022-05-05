class TrieNode:
    def __init__(self):
        self.child = {}
        self.is_word = False

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
        cur_level = self.root
        for c in word:
            if c not in cur_level.child:
                cur_level.child[c] = TrieNode()
            cur_level = cur_level.child[c]

        cur_level.is_word = True



    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        cur_level = self.root
        for c in word:
            if c not in cur_level.child:
                return False
            cur_level = cur_level.child[c]
        return True if cur_level.is_word else False


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cur_level = self.root
        for c in prefix:
            if c not in cur_level.child:
                return False
            cur_level = cur_level.child[c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)