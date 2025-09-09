class Solution:
    def arraySign(self, nums: List[int]) -> int:
        # if len(nums)==0:
        #     return 0
        prod=1
        for each in nums:
            prod *=each
        if prod>0:
            return 1
        elif prod<0:
            return -1
        else:
            return 0