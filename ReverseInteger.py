'''
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Input: x = 123
Output: 321
'''


class Solution:
  def reverse(self, x: int) -> int:
    ans = 0
    sign = -1 if x < 0 else 1
    x *= sign

    while x:
      ans = ans * 10 + x % 10
      x //= 10

    return 0 if ans < -2**31 or ans > 2**31 - 1 else sign * ans
