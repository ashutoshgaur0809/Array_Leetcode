class Solution:
    def maximumSubarraySum(self, a: List[int], k: int) -> int:
        maxi = 0

        if len(set(a)) == 1 and k == 1:
            return a[0]
        
        if len(set(a)) == 1:
            return 0

        else:
            for i in range(len(a)-k+1):
            
                
                sub_a = a[i:i+k]
                set_sub_a = set(sub_a)
                if len(sub_a) == len(set_sub_a):
                    maxi = max(sum(sub_a),maxi)
            
            return maxi
# Example 1:

# Input: nums = [1,5,4,2,9,9,9], k = 3
# Output: 15
# Explanation: The subarrays of nums with length 3 are:
# - [1,5,4] which meets the requirements and has a sum of 10.
# - [5,4,2] which meets the requirements and has a sum of 11.
# - [4,2,9] which meets the requirements and has a sum of 15.
# - [2,9,9] which does not meet the requirements because the element 9 is repeated.
# - [9,9,9] which does not meet the requirements because the element 9 is repeated.
# We return 15 because it is the maximum subarray sum of all the subarrays that meet the conditions
# Example 2:

# Input: nums = [4,4,4], k = 3
# Output: 0
# Explanation: The subarrays of nums with length 3 are:
# - [4,4,4] which does not meet the requirements because the element 4 is repeated.
# We return 0 because no subarrays meet the conditions.

# nums =
# [1,1,1,1,1,1]
# k =
# 1
# Output
# 1
