class Solution:
    def addDigits(self, num: int) -> int:
        if num < 10:
            return num  # Base case: if it's a single-digit number, return it
        total = 0
        while num > 0:
            total += num % 10  # Add last digit
            num //= 10  # Remove last digit
        
        return self.addDigits(total) 