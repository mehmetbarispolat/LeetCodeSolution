"""
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

Example 1:

Input: [1,2,3,1]
Output: true
Example 2:

Input: [1,2,3,4]
Output: false
Example 3:

Input: [1,1,1,3,3,4,3,2,4,2]
Output: true
"""
class Solution:
    def containsDublicate(self,nums):
        """
        type nums: list[int]
        rtype: bool
        """
        #return True if len(nums) != len(set(nums)) else False
        set_nums = set(nums)
        l_nums = list(set_nums)
        l_nums.sort()
        nums.sort()
        if l_nums != nums:
            return True
        else:
            return False

def main():
    arr = [1,5,-2,-4,0]
    s1 = Solution()
    print(s1.containsDublicate(arr))

if __name__ == '__main__':
    main()
    