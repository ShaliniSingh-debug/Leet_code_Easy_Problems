class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l=0
        h=len(nums)-1
        while l<=h:
            mid = (l+h)//2
            if nums[mid]==target:
                return mid
            if nums[mid]>target:
                h=mid-1
            if nums[mid]<target:
                l=mid+1
        return l # since low and high will be at once place if the target is not found return anything either h or l both return he same index

        