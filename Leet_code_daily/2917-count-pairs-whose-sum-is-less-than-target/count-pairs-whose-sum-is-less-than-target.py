class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        count = 0
        nums.sort()
        # !======== Worst Case ==============!
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]+nums[j] < target:
        #             count += 1
            
        # return count
        # !==================Best Case ==============!
        left =0 
        right = len(nums)-1
        while left < right:
            vals = nums[left]+nums[right]
            if vals<target:
                count += right - left
                left += 1
            else:
                right -= 1
        return count
            

    
    




        