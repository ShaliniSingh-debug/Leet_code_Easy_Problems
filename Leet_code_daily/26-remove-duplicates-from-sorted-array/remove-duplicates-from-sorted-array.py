class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        i=0
        for j in range(1,len(nums)):
            if nums[i]!=nums[j]:
                i +=1
                nums[i]= nums[j]
        return i+1
        # this is two pointer approach where i will be decided j will move and once i and i j are not equal i will move and replace nums[i] with nums[j]
            

            

               

        