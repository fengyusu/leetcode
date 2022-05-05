from typing import List

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        n = len(arr2)
        num_dict = {num:i for i,num in enumerate(arr2)}
        arr1 = [[num, num_dict[num] if num in num_dict else n+num] for num in arr1]
        arr1.sort(key=lambda x:x[1])
        return [x[0] for x in arr1]