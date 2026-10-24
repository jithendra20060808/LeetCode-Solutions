class Solution:
    def validateStackSequences(self, pushed: list[int], popped: list[int]) -> bool:
        s = []
        j = 0

        for i in pushed:
            s.append(i)
            while s and s[-1] == popped[j]:
                s.pop()
                j += 1

        if len(s) == 0:
            return True
        else:
            return False