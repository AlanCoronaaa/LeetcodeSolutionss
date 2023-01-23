class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        return sum(filter(lambda x: nums.count(x) == 1, nums))