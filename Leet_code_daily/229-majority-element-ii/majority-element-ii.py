class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)
        num1=0
        num2=1
        ct1=0
        ct2=0
        ans=[]
        for num in nums:
            if num==num1:
                ct1+=1
            elif num==num2:
                ct2+=1
            elif ct1==0:
                num1,ct1=num, 1
            elif ct2==0:
                num2,ct2=num,1
            else:
                ct1-=1
                ct2-=1
        if nums.count(num1)> n//3:
            ans.append(num1)
        if nums.count(num2)>n//3:
            ans.append(num2)
        return ans
        
        



        