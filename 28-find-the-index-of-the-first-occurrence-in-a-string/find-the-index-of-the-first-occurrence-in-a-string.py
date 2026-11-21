class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m = len(needle)
        n = len(haystack)

        for left in range(n - m + 1):
            if haystack[left:left + m] == needle:
                return left

        return -1