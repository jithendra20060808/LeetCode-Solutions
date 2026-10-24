class Solution:
    def makeGood(self, s: str) -> str:
        st =[]
        st.append(s[0])
        for i in range(1,len(s)):
          if len(st)!= 0:
            if (st[-1] == s[i].lower() or st[-1] == s[i].upper()) and st[-1] != s[i]:
                st.pop()
            else:
                st.append(s[i])
          else:
            st.append(s[i])

        return ''.join(st)

