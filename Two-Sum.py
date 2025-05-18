class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        dicts = {}
        for i in range(n):
            val=target-nums[i]
            if val in dicts:
                return [dicts[val],i]
            dicts[nums[i]] =i
           

            

          
            

        