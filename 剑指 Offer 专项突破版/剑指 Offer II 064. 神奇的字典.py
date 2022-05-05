from typing import List


class TrieNode:
    def __init__(self):
        self.child = {}
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur_level = self.root
        for w in word:
            if w not in cur_level.child:
                cur_level.child[w] = TrieNode()
            cur_level = cur_level.child[w]
        cur_level.is_word = True


    def search(self, word):
        change_cnts = 1
        cur_level = self.root
        cur_levels = []
        i = 0
        while i < (len(word)):
            w = word[i]
            if change_cnts:
                if w in cur_level.child:
                    cur_level = cur_level.child[w]
                else:
                    change_cnts = 0
                    if i != len(word) - 1:
                        cur_levels = list(cur_level.child.values())
            else:
                new_cur_levels = []
                for cur_l in cur_levels:
                    if w in cur_l.child:
                        new_cur_levels.append(cur_l.child[w])
                if len(new_cur_levels) == 0:
                    return False
                cur_levels = new_cur_levels
            i += 1
        return False if change_cnts else True


    def search(self, word, cur_level, i, change_cnt):

        if i >= len(word):
            if change_cnt == 1:
                return True
            else:
                return False

        w = word[i]
        found = False
        for k in cur_level.child:
            changes = 0 if k == w else 1
            if change_cnt + changes <= 1 and i < len(word):
                print(w, k, i+1, change_cnt + changes)
                found = found or self.search(word, cur_level.child[k], i+1, change_cnt + changes)

        return found



class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.length_map = {}

    def buildDict(self, dictionary: List[str]) -> None:
        for w in dictionary:
            l = len(w)
            if l not in self.length_map:
                self.length_map[l] = Trie()
            self.length_map[l].insert(w)

    def search(self, searchWord: str) -> bool:
        l = len(searchWord)
        if l not in self.length_map:
            return False
        return self.length_map[l].search(searchWord, self.length_map[l].root, 0, 0)

# Your MagicDictionary object will be instantiated and called as such:
# dict = ["MagicDictionary", "buildDict", "search", "search", "search", "search", "search"]
# [[], [], ["hello"], ["hallo"], ["hell"], ["leetcodd"], ["judge"]]
obj = MagicDictionary()
obj.buildDict(["hello","hallo","leetcode","judge"])
param_2 = obj.search("judge")
print(param_2)