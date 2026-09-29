class Solution:
    def myPow(self, x: float, n: int) -> float:
        N=n
        

        if n<0:
            x = 1/x
            N=-N
        ans=1.0
        current_product=x

        while N >0:
            if N%2==1:
                ans = ans * current_product

            current_product = current_product * current_product
            N = N // 2
        return ans
        
        