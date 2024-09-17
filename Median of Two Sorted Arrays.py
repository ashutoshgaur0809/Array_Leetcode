class Solution:
    def findMedianSortedArrays(self, n1: List[int], n2: List[int]) -> float:

        x = n1+n2
        x.sort()
        if len(x) % 2 != 0:
            mid = len(x) // 2
            # print(x[mid])
            return x[mid]


        if len(x) % 2 == 0:
            mid = len(x) // 2
            s = (x[mid] + x[mid - 1]) / 2
            # print(s)
            return s



# Example 1:

# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
# Example 2:

# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
