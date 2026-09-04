class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        r = 0
        s = 0
        k = []
        while(r<len(nums)):
            s+=nums[r]
            while s>= target:
                length = r -l +1
                k.append(length)
                s-=nums[l]
                l+=1
            r+=1
        return min(k) if k else 0


        