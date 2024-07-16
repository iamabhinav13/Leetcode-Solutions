class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Create a dictionary to store elements and their indices
        num_dict = {}
    
    # Iterate through the array
        for i, num in enumerate(nums):
            # Calculate the complement needed to reach the target
            complement = target - num
        
            # Check if the complement is in the dictionary
            if complement in num_dict:
                # If found, return the indices of the two elements
                return [num_dict[complement], i]
        
            # If complement not found, store the current element and its index in the dictionary
            num_dict[num] = i
    
        # If no solution is found, return an empty list
        return []
