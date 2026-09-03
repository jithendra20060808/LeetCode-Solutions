class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        length = 0
        dic = {}
        for i in range(len(s)):
            c = s[i]
            if c in dic and dic[c] >= l:
                l = dic[c]+1
            else:
                length = max(length,i-l+1)
            dic[c] = i
        return length