class Solution:
    def romanToInt(self, s: str) -> int:
        Numerals = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
        sum = 0 

        def value_of_character(chr):
            return Numerals[chr]

        i = len(s)-1
        while i >= 0:
            if i == 0:
                sum += value_of_character(s[i])
                i -= 1
            elif value_of_character(s[i]) > value_of_character(s[i-1]):
                sum += (value_of_character(s[i]) - value_of_character(s[i-1]))
                i -= 2
            else:
                sum += value_of_character(s[i])
                print(value_of_character(s[i]))
                i -= 1
        
        return sum