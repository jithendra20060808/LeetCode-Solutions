class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        if len(s) == 0 or len(s) == 1:
            return False
        elif len(s)%2!= 0:
            return False
        else:
         for i in range(len(s)):
            if s[i] == '(':
                st.append(")")
            elif s[i] == "[":
                st.append("]")
            elif s[i] == '{':
                st.append('}')
            elif s[i] == ")" and st and  st[-1] == ")":
                st.pop()
            elif s[i] == "}" and st and  st[-1] == "}":
                st.pop()
            elif s[i] == "]" and st and st[-1] == "]":
                st.pop()
            else:
                return False
        if len(st) == 0:
            return True
        else:
            return False
            
            

        