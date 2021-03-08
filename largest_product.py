"""
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""
class Solution:
    def max_product(self, arr):
        if len(arr) > 0:
            output = arr[0]
        ma, mi = 1, 1
        for a in arr:
            ma, mi = max(a, a*ma, a*mi), min(a, a*ma, a*mi)
            output = max(output, ma, mi)
        return output    


if __name__ == "__main__":
    nums = list(range(10000))
    s1 = Solution()
    s1.max_product(nums)