from collections import deque

class RecentCounter0:

    def __init__(self):
        self.queue = []
        self.n = 0
        self.time_win = 3000

    def ping(self, t: int) -> int:
        self.queue.append(t)
        self.n += 1
        res_count = 0
        start = t-self.time_win
        for i in range(self.n-1,-1,-1):
            if self.queue[i] >= start:
                res_count += 1
        return res_count


class RecentCounter:

    def __init__(self):
        self.queue = deque()

    def ping(self, t: int) -> int:
        self.queue.append(t)
        while self.queue[0] < t-3000:
            self.queue.popleft()
        return len(self.queue)


if __name__ == '__main__':
    rc = RecentCounter()
    print(rc.ping(1))
    print(rc.ping(100))
    print(rc.ping(3001))
    print(rc.ping(3002))

