class Solution:
    def calPoints(self, operations: list[str]) -> int:
        x = []
        for i in operations:
            if i == "+":
                m=sum([x[-1],x[-2]])
                x.append(m)
            elif i == "D":
                x.append(x[-1]*2)
            elif i == "C":
                x.pop()
            else:
                x.append(int(i))
        return sum(x)
        