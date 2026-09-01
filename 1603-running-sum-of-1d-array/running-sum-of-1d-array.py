class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        summ = 0
        l = []
        for i in nums:
            summ+=i
            l.append(summ)
        return l
        