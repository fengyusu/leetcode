
class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.val_list = []
        self.cur_sum = 0
        self.cur_len = 0


    def next(self, val: int) -> float:
        if self.cur_len < self.size:
            self.cur_len += 1
            self.cur_sum += val
        else:
            self.cur_sum += val
            self.cur_sum -= self.val_list[0]
        self.val_list.append(val)
        self.val_list = self.val_list[-self.size:]
        return self.cur_sum / self.cur_len



# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)