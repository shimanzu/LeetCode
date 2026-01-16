class Solution:
    def reverse(self, x: int) -> int:
        neg = False
        if x < 0:
            neg = True
            x *= -1
        t = 1
        rev = 0
        while x > 0:
            rev = rev * 10 + x%10
            x //= 10
        if rev > 2147483647:
            return 0
        if neg:
            rev *= -1
        return rev
