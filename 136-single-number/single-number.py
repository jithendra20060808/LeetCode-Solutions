class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dct = {}
        for i in nums:
            if i in dct:
                dct[i]+=1
            else:
                dct[i]=1
        for i,j in dct.items():
            if j == 1:
              return i

        