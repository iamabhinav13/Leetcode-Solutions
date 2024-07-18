class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        
        # Find the shortest string in the array
        min_length = min(len(s) for s in strs)
        
        # Compare characters from left to right
        prefix = ""
        for i in range(min_length):
            current_char = strs[0][i]  # Compare characters from the first string
            for string in strs[1:]:
                if string[i] != current_char:
                    return prefix
            prefix += current_char
        
        return prefix
