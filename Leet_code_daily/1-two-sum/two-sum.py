class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_hasmap={}
        for i, num in enumerate(nums):
            seen_num= target-nums[i]
            if seen_num in seen_hasmap:
                return [seen_hasmap[seen_num],i] # get the index of found value from hasmap and i which is now containing the value 
            seen_hasmap[num]=i
        
        