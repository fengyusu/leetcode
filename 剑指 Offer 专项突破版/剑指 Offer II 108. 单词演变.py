from typing import List
from collections import deque
from collections import defaultdict


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def addWord(word: str):
            if word not in wordId:
                nonlocal nodeNum
                wordId[word] = nodeNum
                nodeNum += 1

        def addEdge(word: str):
            addWord(word)
            id1 = wordId[word]
            chars = list(word)
            for i in range(len(chars)):
                tmp = chars[i]
                chars[i] = "*"
                newWord = "".join(chars)
                addWord(newWord)
                id2 = wordId[newWord]
                edge[id1].append(id2)
                edge[id2].append(id1)
                chars[i] = tmp

        wordId = dict()
        edge = defaultdict(list)
        nodeNum = 0

        for word in wordList:
            addEdge(word)

        addEdge(beginWord)
        if endWord not in wordId:
            return 0

        dis = [float("inf")] * nodeNum
        beginId, endId = wordId[beginWord], wordId[endWord]
        dis[beginId] = 0

        que = deque([beginId])
        while que:
            x = que.popleft()
            if x == endId:
                return dis[endId] // 2 + 1
            for it in edge[x]:
                if dis[it] == float("inf"):
                    dis[it] = dis[x] + 1
                    que.append(it)

        return 0

class Solution:

    def is_connect(self, w1, w2):
        if len(w1) != len(w2):
            return False
        diff_cnt = 0
        for i in range(len(w1)):
            if w1[i] != w2[i]:
                diff_cnt += 1
        return True if diff_cnt == 1 else False

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        if beginWord in wordList:
            wordList.pop(wordList.index(beginWord))


        q_begin = deque()
        q_begin.append(beginWord)
        word_set_begin = set(wordList)
        level_begin = 1

        q_end = deque()
        q_end.append(endWord)
        word_set_end = word_set_begin.copy()
        word_set_end.remove(endWord)
        level_end = 1


        print("word_set ", word_set_begin)
        print("word_set_end ", word_set_end)


        while q_begin and q_end:

            cur_level_connect_word = set()
            level_begin += 1
            cur_level_size = len(q_begin)
            for i in range(cur_level_size):
                cur_w = q_begin.popleft()
                for cand_w in word_set_begin:
                    if self.is_connect(cur_w, cand_w):
                        if cand_w in q_end:
                            return level_begin + level_end - 1
                        cur_level_connect_word.add(cand_w)
                        q_begin.append(cand_w)
            for connect_word in cur_level_connect_word:
                word_set_begin.remove(connect_word)

            # print("level_begin ", level_begin)
            # print("q_begin ", q_begin)
            # print("word_set_begin ", word_set_begin)
            # print("*" * 10, "\r\n")


            cur_level_connect_word = set()
            level_end += 1
            cur_level_size = len(q_end)
            for i in range(cur_level_size):
                cur_w = q_end.popleft()
                for cand_w in word_set_end:
                    if self.is_connect(cur_w, cand_w):
                        if cand_w in q_begin:
                            return level_begin + level_end - 1
                        cur_level_connect_word.add(cand_w)
                        q_end.append(cand_w)
            for connect_word in cur_level_connect_word:
                word_set_end.remove(connect_word)


            # print("q_end ", q_end)
            # print("level_end ", level_end)
            # print("word_set_end ", word_set_end)
            # print("*"*30, "\r\n\r\n")





        return 0

sln = Solution()
print(sln.ladderLength("hit",
"cog",
["hot","dot","dog","lot","log","cog"]))





