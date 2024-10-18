from itertools import combinations

# Function to generate all possible subsets and find the subset with maximum OR operation value
def solutions(nums):
    subsets = []
    n = len(nums)
    
    # If all elements in the list are the same, return (element^length) - 1
    if len(set(nums)) == 1:
        return pow(nums[0], len(nums)) - 1
    
    # Generate all subsets of nums from size 1 to n
    print("All Possible Subsets -->")
    for r in range(1, n + 1):
        subsets.extend(list(combinations(nums, r)))
    
    subsets = set(subsets)  # To ensure unique subsets
    print(subsets)
    
    # Variables to store max OR value and the count of subsets giving this max value
    max_or = 0
    max_count = 0
    or_results = []
    
    # Iterate through each subset and calculate the bitwise OR for each
    for subset in subsets:
        subset_or = subset[0]
        
        # Apply bitwise OR between all elements of the subset
        for num in subset[1:]:
            subset_or |= num
        
        # Store the OR result and track the max OR value
        or_results.append(subset_or)
        print(f"Bitwise OR of {subset} is: {subset_or}")
        
        if subset_or > max_or:
            max_or = subset_or
            max_count = 1  # Reset the count as we found a new max OR value
        elif subset_or == max_or:
            max_count += 1
    
    # Printing intermediate results
    print("All possible OR operations results -->", or_results)
    print("Maximum OR Operation value is -->", max_or)
    print("Total Subsets that yield the maximum OR value -->", max_count)
    
    return max_or, max_count

# Example usage
nums = [3, 1]
max_or_value, max_count = solutions(nums)
print(f"Maximum OR value: {max_or_value}, Subsets Count: {max_count}")


# Example 1:

# Input: nums = [3,1]
# Output: 2
# Explanation: The maximum possible bitwise OR of a subset is 3. There are 2 subsets with a bitwise OR of 3:
# - [3]
# - [3,1]
# Example 2:

# Input: nums = [2,2,2]
# Output: 7
# Explanation: All non-empty subsets of [2,2,2] have a bitwise OR of 2. There are 23 - 1 = 7 total subsets.
# Example 3:

# Input: nums = [3,2,1,5]
# Output: 6
# Explanation: The maximum possible bitwise OR of a subset is 7. There are 6 subsets with a bitwise OR of 7:
# - [3,5]
# - [3,1,5]
# - [3,2,5]
# - [3,2,1,5]
# - [2,5]
# - [2,1,5]



# Optimized Solutions

# from itertools import combinations
# from typing import List

# class Solution:
#     def countMaxOrSubsets(self, nums: List[int]) -> int:
#         # Handle the case when there is only one number in the input
#         if len(nums) == 1:
#             return 1  # Only one subset is possible, the number itself
        
#         # Step 1: Generate all subsets
#         subsets = []
#         n = len(nums)
        
#         # Generate all subsets (combinations) from 1 element to n elements
#         for r in range(1, n + 1):
#             subsets.extend(list(combinations(nums, r)))
        
#         # Step 2: Find the maximum OR value and count subsets that match it
#         max_or = 0
#         max_count = 0
        
#         for subset in subsets:
#             subset_or = subset[0]
#             # Compute the OR for the current subset
#             for num in subset[1:]:
#                 subset_or |= num
            
#             # Update the maximum OR value and count how many subsets give this value
#             if subset_or > max_or:
#                 max_or = subset_or
#                 max_count = 1  # Reset the count since we found a new max OR
#             elif subset_or == max_or:
#                 max_count += 1  # Increment the count for max OR subsets
        
#         # Return the count of subsets that yield the maximum OR value
#         return max_count
