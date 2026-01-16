class Solution:
    def isPalindrome(self, x: int) -> bool:
        number = []
        if x < 0:
            return False
        while x > 0:
            number.append(x%10)
            x //= 10

        number = number[::-1]

        for i in range(0, len(number)//2):
            if number[i] != number[len(number) - 1 - i]:
                return False

        return True