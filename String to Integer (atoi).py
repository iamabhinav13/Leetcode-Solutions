class Solution:
    def myAtoi(self, s):
        # Initialize the index, sign, and result
        i, sign, result = 0, 1, 0
        n = len(s)
        
        # Step 1: Ignore leading whitespace
        while i < n and s[i] == ' ':
            i += 1
        
        # Step 2: Check for sign
        if i < n and (s[i] == '-' or s[i] == '+'):
            sign = -1 if s[i] == '-' else 1
            i += 1
        
        # Step 3: Convert digits to integer
        while i < n and s[i].isdigit():
            result = result * 10 + int(s[i])
            i += 1
        
        # Apply the sign
        result *= sign
        
        # Step 4: Clamp the result to the 32-bit signed integer range
        INT_MAX, INT_MIN = 2**31 - 1, -2**31
        if result > INT_MAX:
            return INT_MAX
        if result < INT_MIN:
            return INT_MIN
        
        return result
