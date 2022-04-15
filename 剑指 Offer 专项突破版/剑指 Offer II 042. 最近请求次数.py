

class RecentCounter:

    def __init__(self):
        self.req_list = []

    def ping(self, t: int) -> int:
        self.req_list.append(t)
        for i in range(len(self.req_list)):
            if self.req_list[i] >= t-3000:
                self.req_list = self.req_list[i:]
                break
        return len(self.req_list)

    def lower_bound(self, nums, target):
        low, high = 0, len(nums) - 1
        pos = len(nums)
        while low < high:
            mid = (low + high) // 2
            if nums[mid] < target:
                low = mid + 1
            else:  # >=
                high = mid
                # pos = high
        if nums[low] >= target:
            pos = low
        return pos

    def ping(self, t: int) -> int:
        self.req_list.append(t)
        edge_index = self.lower_bound(self.req_list, t-3000)
        self.req_list = self.req_list[edge_index:]
        return len(self.req_list)




# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)