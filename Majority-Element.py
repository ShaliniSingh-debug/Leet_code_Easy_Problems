class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        n=len(nums)
        number={}
        if n==1:
            return nums[0]
        for i in range(n):
            if nums[i] in number:
                number[nums[i]] =number[nums[i]]+1
            else:
                number[nums[i]]=1

                
        maxNum=nums[0]
        for i , val in number.items():
            if val >n//2:
                maxNum=i
        return maxNum



            
        