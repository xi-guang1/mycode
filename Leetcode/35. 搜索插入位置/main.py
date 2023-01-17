from typing import *

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        mid = (left + right) // 2
        if nums[right] < target:
            return right + 1
        elif nums[left] > target:
            return 0
        while nums[mid] != target:
            if nums[mid] > target:
                right = mid
                mid = (left + right) // 2
            else:
                left = mid
                mid = (left + right) // 2
        return mid