class Solution:
    def minElement(self, nums: List[int]) -> int:
        least_integer=nums[0]
        
        newnum =[]
        for i in range(len(nums)):
            if nums[i]<10:
                if nums[i] < least_integer:
                    least_integer = nums[i]
            else:
                n=nums[i]
                f=0
                while n>0:
                    f += n%10
                    n=n//10
                least_integer=min(f,least_integer)
        return least_integer
       
                
        