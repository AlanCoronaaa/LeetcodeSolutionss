class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""

        for a in zip(*strs):
            if len(set(a)) == 1:
                result += a[0]
            else:
                return result

        return result