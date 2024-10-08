class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        closest_sum = float('inf')
        min_diff = float('inf')
        n = len(nums)
        
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left, right = i + 1, n - 1
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                diff = abs(current_sum - target)
                
                if diff < min_diff:
                    min_diff = diff
                    closest_sum = current_sum
                
                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
                else:
                    return target
        
        return closest_sum
