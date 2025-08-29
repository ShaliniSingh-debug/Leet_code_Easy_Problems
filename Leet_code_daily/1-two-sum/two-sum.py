class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        twosumDict={}
        for i,j in enumerate(nums):
            presentval=target-nums[i]
            if presentval in twosumDict:
                return [twosumDict[presentval],i]
            twosumDict[j]=i
        