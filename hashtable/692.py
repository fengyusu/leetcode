from collections import Counter

class Solution:

    def compare(self, key1, key2):
        if self.word_table[key1] == self.word_table[key2]:
            return key1 < key2
        else:
            return self.word_table[key1] > self.word_table[key2]

    def swap(self, arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]

    def heap_pop(self):
        self.swap(self.keys, 0, len(self.keys)-1)
        res = self.keys.pop()
        self.heapify(self.keys, 0)
        return res

    def heapify(self, arr, index):
        largest = index
        left = 2 * index + 1
        right = 2 * index + 2
        if left < len(arr) and self.compare(arr[left],arr[largest]):
            largest = left
        if right < len(arr) and self.compare(arr[right],arr[largest]):
            largest = right
        if index != largest:
            self.swap(arr, largest, index)
            self.heapify(arr, largest)

    def build_heap(self):
        self.keys = list(self.word_table.keys())
        for i in range(len(self.keys)//2, -1, -1):
            self.heapify(self.keys, i)
            print("index", i)
            print(self.keys)
            values = []
            for k in self.keys:
                values.append(self.word_table[k])
            print(values)

    def topKFrequent0(self, words, k: int):
        self.word_table = {}
        for w in words:
            if w in self.word_table.keys():
                self.word_table[w] += 1
            else:
                self.word_table.setdefault(w, 1)
        print(self.word_table)
        self.build_heap()

        print(self.keys)
        res = []
        for i in range(k):
            res.append(self.heap_pop())
        return res

    def sort_key(self, key):
        return (-self.word_table[key], key)

    def topKFrequent(self, words, k: int):
        self.word_table = {}
        for w in words:
            if w in self.word_table.keys():
                self.word_table[w] += 1
            else:
                self.word_table.setdefault(w, 1)
        self.keys = list(self.word_table.keys())
        # self.keys.sort(key=lambda w: (-self.word_table[w], w))
        self.keys.sort(key=self.sort_key)
        return self.keys[:k]


if __name__ == '__main__':
    str = ["plpaboutit","jnoqzdute","sfvkdqf","mjc","nkpllqzjzp","foqqenbey","ssnanizsav","nkpllqzjzp","sfvkdqf","isnjmy","pnqsz","hhqpvvt","fvvdtpnzx","jkqonvenhx","cyxwlef","hhqpvvt","fvvdtpnzx","plpaboutit","sfvkdqf","mjc","fvvdtpnzx","bwumsj","foqqenbey","isnjmy","nkpllqzjzp","hhqpvvt","foqqenbey","fvvdtpnzx","bwumsj","hhqpvvt","fvvdtpnzx","jkqonvenhx","jnoqzdute","foqqenbey","jnoqzdute","foqqenbey","hhqpvvt","ssnanizsav","mjc","foqqenbey","bwumsj","ssnanizsav","fvvdtpnzx","nkpllqzjzp","jkqonvenhx","hhqpvvt","mjc","isnjmy","bwumsj","pnqsz","hhqpvvt","nkpllqzjzp","jnoqzdute","pnqsz","nkpllqzjzp","jnoqzdute","foqqenbey","nkpllqzjzp","hhqpvvt","fvvdtpnzx","plpaboutit","jnoqzdute","sfvkdqf","fvvdtpnzx","jkqonvenhx","jnoqzdute","nkpllqzjzp","jnoqzdute","fvvdtpnzx","jkqonvenhx","hhqpvvt","isnjmy","jkqonvenhx","ssnanizsav","jnoqzdute","jkqonvenhx","fvvdtpnzx","hhqpvvt","bwumsj","nkpllqzjzp","bwumsj","jkqonvenhx","jnoqzdute","pnqsz","foqqenbey","sfvkdqf","sfvkdqf"]

    solution = Solution()
    result = solution.topKFrequent(str, 5)
    print(result)