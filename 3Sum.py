class Solution:
    def threeSum(self, nums):
        result = set()
        nums.sort()
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            s = set()
            for num in nums[i+1:]:
                if -nums[i] - num in s:
                    result.add(tuple([nums[i], -nums[i]-num, num]))
                s.add(num)
        return [i for i in result]