class Solution:
    def maxDepth(self, s: str) -> int:
        m = []
        count = 0
        if "(" in s or ")" in s:
         for i in s:
         
            if i == "(":
                count+=1
                m.append(count)
            elif i ==")":
                count-=1
            
         return max(m)
        else:
            return 0
        