class Solution:
    def isPalindrome(self, x: int) -> bool:
        z = str(x)
        if z == z[::-1]:
            return True
        else:
            return False
        