class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        m = []
        count = 0
        if "(" in s or ")" in s:
         for i in s:
         
            if i == "(":
                stack.append(i)
                count+=1
                m.append(count)
            elif i ==")":
                stack.pop()
                count-=1
            
         return max(m)
        else:
            return 0
        