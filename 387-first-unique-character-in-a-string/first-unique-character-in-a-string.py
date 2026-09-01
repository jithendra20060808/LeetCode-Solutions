class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        l = []
        for i in s:
            if i not in d:
                d[i] =1
            else :
                d[i]+=1
        for k,v in d.items():
            if v == 1:
                l.append(k)
        if len(l)!= 0:
            a = l[0]
            z = s.index(a)
            return z
        else:
            return -1

        