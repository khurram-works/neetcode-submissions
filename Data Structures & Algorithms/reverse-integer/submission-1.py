class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        revNum = 0
        while x != 0:
            dig = x % 10
            revNum = revNum * 10 + dig 
            x = x // 10                 
            

        reversed_x = sign * revNum

        if reversed_x < -2**31 or reversed_x > 2**31 - 1:
            return 0
            
        return reversed_x

        