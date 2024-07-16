class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0

        char_index_map = {}
        max_length = 0
        start = 0

        for i, char in enumerate(s):
            if char in char_index_map and char_index_map[char] >= start:
                start = char_index_map[char] + 1

            char_index_map[char] = i
            current_length = i - start + 1
            max_length = max(max_length, current_length)
        return max_length
