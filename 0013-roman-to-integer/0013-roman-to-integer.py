class Solution:
    def romanToInt(self, s: str) -> int:
        # 1. Define the mapping of Roman numerals to integers
        roman_map = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        
        total = 0
        n = len(s)
        
        # 2. Iterate through the string
        for i in range(n):
            # Check if we are NOT at the last character AND 
            # the current value is less than the next value
            if i + 1 < n and roman_map[s[i]] < roman_map[s[i + 1]]:
                total -= roman_map[s[i]]
            else:
                total += roman_map[s[i]]
                
        return total