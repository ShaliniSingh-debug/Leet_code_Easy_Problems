class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        count = len(baskets)
        # first try to get 
        for i in range(len(fruits)):
            for j in range(len(baskets)):
                if fruits[i]<=baskets[j]:
                    baskets[j]=0
                    count -=1
                    break
        return count
                
        