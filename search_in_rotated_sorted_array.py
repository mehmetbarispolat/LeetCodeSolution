'''
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1
'''
class Solution(object):

    @classmethod
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        first_num = nums[0]
                    
        if not target in nums:
            return -1
        
        if target < first_num:
            for idx in range(len(nums)-1, -1, -1):
                if nums[idx] == target:
                    return idx
        else:
            for idx, num in enumerate(nums):
                if target == num:
                    return idx


### ------------ DELETE THESE BLOCKS(49-59) WHEN SEND TO LEET CODE ------------ ###
if __name__ == "__main__":
    nums_list = [
        [4,5,6,7,0,1,2],
        [4,5,6,7,0,1,2],
        [1]
    ]
    target_list = [0, 3, 0]
    for i in range(len(nums_list)):
        result = Solution.search(nums_list[i], target_list[i])
        print(result)