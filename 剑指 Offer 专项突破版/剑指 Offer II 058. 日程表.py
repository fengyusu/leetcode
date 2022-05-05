

class MyCalendar:

    def __init__(self):
        self.calendar  = []

    def upper_bound(self, nums, target):
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid][0] == target:
                high = mid - 1
            elif nums[mid][0] < target:
                low = mid + 1
            elif nums[mid][0] > target:
                high = mid - 1
        return low

    def lower_bound(self, nums, target):
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid][1] == target:
                low = mid + 1
            elif nums[mid][1] < target:
                low = mid + 1
            elif nums[mid][1] > target:
                high = mid - 1
        return high

    def book(self, start: int, end: int) -> bool:
        # print("self.calendar ", self.calendar, start, end)
        if len(self.calendar) == 0:
            self.calendar.append([start, end])
            return True
        upper_index = self.upper_bound(self.calendar, end)
        lower_index = self.lower_bound(self.calendar, start)
        # print(lower_index, upper_index, )
        if upper_index != 0 and start < self.calendar[upper_index-1][1]:
            return False
        if lower_index != len(self.calendar)-1 and end > self.calendar[lower_index+1][0]:
            return False

        self.calendar.insert(upper_index, [start, end])
        return True





# Your MyCalendar object will be instantiated and called as such:
obj = MyCalendar()
# print(obj.book(10,20))
# print(obj.book(15,25))
# print(obj.book(20,30))
# print(obj.book(0,5))

data = [[47,50],[33,41],[39,45],[33,42],[25,32],[26,35],[19,25],[3,8],[8,13],[18,27]]
for i in range(len(data)):
    print(obj.book(data[i][0], data[i][1]))


