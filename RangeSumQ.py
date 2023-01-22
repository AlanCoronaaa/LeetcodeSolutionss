class NumArray(object):
    def __init__(self, nums):
        self.update = nums.__setitem__
        self.sumRange = lambda i, j: sum(nums[i:j+1])


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)