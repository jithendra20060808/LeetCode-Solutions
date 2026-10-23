class Solution:
    def buildArray(self, target: list[int], n: int) -> list[str]:
        d = []
        count = 0

        for i in range(1, n + 1):
            if count == len(target):
                break

            d.append("Push")

            if i == target[count]:
                count += 1
            else:
                d.append("Pop")

        return d
    

            




        
