class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while len(s) > 2:
            s = "".join(str((int(s[i]) + int(s[i+1])) % 10) for i in range(len(s) - 1))
            if len(set(s)) == 1:  # Check if all digits in the sequence are the same
                return True
        return False
            
            
            
            
            

        