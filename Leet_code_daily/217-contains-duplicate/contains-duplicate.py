class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        findDupes= set()
        for num in nums:
            if num in findDupes:
                return True
            findDupes.add(num)
        return False