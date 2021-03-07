"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Example 2:

Input: nums = [1]
Output: 1
Example 3:

Input: nums = [0]
Output: 0
Example 4:

Input: nums = [-1]
Output: -1
Example 5:

Input: nums = [-100000]
Output: -100000

Constraints:

1 <= nums.length <= 3 * 104
-105 <= nums[i] <= 105
 
Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""
class Solution:
    def max_sub_array(self,nums):
        l = len(nums)
        local_max = 0
        global_max = min(nums)
        
        for i in range(l):
            local_max = max( nums[i], nums[i] + local_max )
            if local_max > global_max:
                global_max = local_max
        return global_max
        
def main():
    liste = [-2,1,-3,4,-1,2,1,-5,4]
    s2 = Solution()
    result2 = s2.max_sub_array(liste)
    print(result2)
    
if __name__ == "__main__":
    main()