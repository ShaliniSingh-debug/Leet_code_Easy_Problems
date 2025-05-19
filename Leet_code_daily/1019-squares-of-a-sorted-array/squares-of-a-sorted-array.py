class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right= len(nums)-1
        final=[]
        while left<= right:
            if abs(nums[left])>abs(nums[right]):
                final.append(nums[left]**2)
                left +=1
            else:
                final.append(nums[right]**2)
                right = right-1
        return final[::-1]

        