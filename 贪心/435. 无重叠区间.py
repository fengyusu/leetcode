

class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        if len(intervals) <= 1:
            return 0
        intervals.sort(key=lambda x:x[1])
        del_counts = 0
        last_edge = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] < last_edge:
                del_counts += 1
            else:
                last_edge = intervals[i][1]
        return del_counts

