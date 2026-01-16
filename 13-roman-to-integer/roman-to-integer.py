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
        i = len(s)-1
        while i >= 0:
            if i == 0:
                sum += Numerals[s[i]]
                i -= 1
            elif Numerals[s[i]] > Numerals[s[i-1]]:
                sum += (Numerals[s[i]] - Numerals[s[i-1]])
                i -= 2
            else:
                sum += Numerals[s[i]]
                i -= 1
        
        return sum