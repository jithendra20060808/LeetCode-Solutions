class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        s=[]
        for i in nums:
            s.append(i**2)
        l = sorted(s)
        return l
        
        