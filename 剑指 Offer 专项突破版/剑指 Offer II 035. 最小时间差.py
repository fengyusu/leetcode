from typing import List

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        time_minutes = []
        timePoints = sorted(timePoints)
        last_minutes = int(timePoints[-1].split(':')[0]) * 60 + int(timePoints[-1].split(':')[1]) - 24*60
        for t in timePoints:
            minutes = int(t.split(':')[0]) * 60 + int(t.split(':')[1])
            time_minutes.append(minutes-last_minutes)
            last_minutes = minutes

        return min(time_minutes)