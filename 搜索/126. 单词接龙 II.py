
from collections import deque
class Solution:
    def isConnect(self, w1, w2):
        if len(w1) != len(w2):
            return False
        dif_count = 0
        for i in range(len(w1)):
            if w1[i] != w2[i]:
                dif_count += 1
        if dif_count == 1:
            return True
        return False

    def backTracking(self, src, dst, graph, path, res):
        if src == dst:
            res.append(path.copy())
            return
        for w in graph[src]:
            path.append(w)
            self.backTracking(w, dst, graph, path, res)
            path.pop()


    def findLadders(self, beginWord: str, endWord: str, wordList):
        word_set = set(wordList)
        if endWord not in word_set:
            return []
        if beginWord in word_set:
            word_set.remove(beginWord)
        word_graph = {}
        word_graph[beginWord] = set()
        for w in word_set:
            word_graph[w] = set()
        q = deque()
        q.append(beginWord)

        found = False
        while len(q) and not found:
            n_q = len(q)
            cur_level = set()
            print("************")
            print(q)
            print(word_set)

            while n_q:
                n_q -= 1
                w = q.popleft()

                for s in word_set:
                    if self.isConnect(w,s):
                        word_graph[w].add(s)
                        if s == endWord:
                            found = True
                        else:
                            cur_level.add(s)
                            q.append(s)

            print(word_graph)
            print(cur_level)
            # if found:
            #     break
            for w in cur_level:
                word_set.remove(w)

        print(word_graph)
        res = []
        if found:
            path = [beginWord]
            self.backTracking(beginWord, endWord, word_graph, path, res)
        return res

if __name__ == '__main__':
    beginWord = "red"
    endWord = "tax"
    wordList = ["ted", "tex", "red", "tax", "tad", "den", "rex", "pee"]


    solution = Solution()
    res = solution.findLadders(beginWord,endWord,wordList)
    print(res)