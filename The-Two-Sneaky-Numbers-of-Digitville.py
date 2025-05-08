class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        # find duplicates create a dict and put the dict then check if the value is there inthe list if its there save to anu
        seen = set()
        duplicate = set()
        for items in nums:
            if items in seen:
                duplicate.add(items)
            else:
                seen.add(items)
        return list(duplicate)

        
            
        