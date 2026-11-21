class Solution:
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        queue = []
        for i in range(len(tickets)):
            queue.append(i)
        time = 0
        while queue:
            idx = queue.pop(0)
            tickets[idx]-=1
            time+=1
            if tickets[idx] == 0:
                if idx == k:
                    return time
            else:
                queue.append(idx)