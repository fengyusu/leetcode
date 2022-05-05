from typing import List

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

class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        sorted_words = sorted(words, key=lambda x : len(x), reverse=True)
        trie = Trie()
        res = 0
        for w in sorted_words:
            w = w[::-1]
            if not trie.startsWith(w):
                res += len(w)+1
                trie.insert(w)
        return res

sln = Solution()
print(sln.minimumLengthEncoding(["time", "me", "bell"]))
print("abc"[::-1])