import itertools


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for idx1, idx2 in itertools.product(range(len(nums)), range(len(nums))):
            if idx1 == idx2:
                continue
            currSum = nums[idx1] + nums[idx2]
            if currSum == target:
                return [idx1, idx2]
