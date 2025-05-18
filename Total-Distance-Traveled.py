class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        distance_traveled = 0
        while mainTank >=5:
            distance_traveled +=5*10
            mainTank -= 5 #
            if additionalTank >0:
                mainTank +=1
                additionalTank -=1
        distance_traveled +=mainTank*10
        return distance_traveled
      


        


 


        