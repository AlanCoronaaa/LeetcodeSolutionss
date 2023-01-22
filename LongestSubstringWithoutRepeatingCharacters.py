'''Given a string s, find the length of the longest
substring
 without repeating characters.


 Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
'''
import collections


class Solution:
  def lengthOfLongestSubstring(self, s: str) -> int:
      ans = 0
      count = collections.Counter()

      1=0
      for r, c in enumerate(s):
          count[c] += 1
          while count[c] >1:
              count[s[1]] -= 1
              1+=1
            ans = max(ans, r - 1 + 1 )

          return ans
