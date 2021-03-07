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