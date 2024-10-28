from typing import List

class Solution:
    def longestSquareStreak(self, a: List[int]) -> int:
        # Convert the list to a set for O(1) lookups
        num_set = set(a)

        # Use a set to store unique valid numbers
        square_streak = set()

        for num in num_set:
            if (num * num) in num_set:
                square_streak.add(num)
                square_streak.add(num * num)

        # If no valid square streak is found, return -1
        if not square_streak:
            return -1

        return len(square_streak)

# Function to read user input
def main():
    input_string = input("Enter a list of integers separated by spaces: ")
    # Convert the input string to a list of integers
    input_list = list(map(int, input_string.split()))
    
    # Create a Solution object
    solution = Solution()
    
    # Get the result from longestSquareStreak
    result = solution.longestSquareStreak(input_list)
    
    # Print the result
    print(f"The length of the longest square streak is: {result}")

if __name__ == "__main__":
    main()


# Example 1:
# //
# // Input: nums = [4,3,6,16,8,2]
# // Output: 3
# // Explanation: Choose the subsequence [4,16,2]. After sorting it, it becomes [2,4,16].
# // - 4 = 2 * 2.
# // - 16 = 4 * 4.
# // Therefore, [4,16,2] is a square streak.
# // It can be shown that every subsequence of length 4 is not a square streak.
# // Example 2:
# //
# // Input: nums = [2,3,5,6,7]
# // Output: -1
# // Explanation: There is no square streak in nums so return -1.
