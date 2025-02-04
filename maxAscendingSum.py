class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
            max_sum = current_sum = nums[0]

            for i in range(1, len(nums)):
                if nums[i] > nums[i - 1]:  # Continue the ascending subarray
                    current_sum += nums[i]
                else:  # Reset to the new subarray
                    current_sum = nums[i]
                
                max_sum = max(max_sum, current_sum)  # Update max sum

            return max_sum
                
