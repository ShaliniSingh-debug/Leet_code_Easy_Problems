class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if  len(nums)<2:
            return 0
        nums.sort()
        res=0
        for i in range(1,len(nums)):
            gap = nums[i] - nums[i - 1]
        # Update max_gap if the current gap is larger
            res = max(res, gap)
        return res
            
        

            
        