class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        summ = 0
        l = []
        for i in range(len(accounts)):
            l.append(sum(accounts[i]))
        return max(l)



        