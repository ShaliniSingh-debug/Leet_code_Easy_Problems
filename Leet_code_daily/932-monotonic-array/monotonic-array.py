class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        flag1=flag2=True
        for i in range(len(nums)-1):
            if nums[i]<nums[i+1]:
                flag1= False
            if nums[i]>nums[i+1]:
                flag2=False
        return flag1 or flag2
        