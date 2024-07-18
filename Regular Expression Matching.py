class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m, n = len(s), len(p)
        
        # Initialize previous and current row arrays
        prev = [False] * (n + 1)
        curr = [False] * (n + 1)
        
        # Empty pattern matches empty string
        prev[0] = True
        
        # Handle patterns with '*'
        for j in range(2, n + 1):
            if p[j - 1] == '*':
                prev[j] = prev[j - 2]
        
        # Fill the DP rows
        for i in range(1, m + 1):
            curr[0] = False
            for j in range(1, n + 1):
                if p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                    curr[j] = prev[j - 1]
                elif p[j - 1] == '*':
                    curr[j] = curr[j - 2] or (prev[j] if p[j - 2] == s[i - 1] or p[j - 2] == '.' else False)
                else:
                    curr[j] = False
            prev, curr = curr, [False] * (n + 1)
        
        return prev[n]
