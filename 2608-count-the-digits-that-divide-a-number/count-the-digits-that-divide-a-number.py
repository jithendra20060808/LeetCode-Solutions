class Solution:
    def countDigits(self, num: int) -> int:
        dic = {}
        nums = str(num)
        l = list(nums)
        c = []
        summ = 0
        for i in l:
            if num%int(i)==0:
                c.append(i)
        for i in c:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i]+=1
        for key,value in dic.items():
            summ+=value
        return summ
        

            



        