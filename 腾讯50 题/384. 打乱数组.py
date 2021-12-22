from typing import List
import random


class Solution:

    def __init__(self, nums: List[int]):
        self.array = nums
        self.origin = nums.copy()


    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        self.array = self.origin.copy()
        return self.array


    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        n = len(self.array)
        for i in range(n):
            swap_idx = random.randint(i, n-1)
            self.array[i],self.array[swap_idx] = self.array[swap_idx],self.array[i]
        return self.array
