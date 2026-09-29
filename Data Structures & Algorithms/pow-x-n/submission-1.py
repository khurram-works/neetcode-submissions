# class Solution:
#     def myPow(self, x: float, n: int) -> float:
#         N=n
        

#         if n<0:
#             x = 1/x
#             N=-N
#         ans=1.0
#         current_product=x

#         while N >0:
#             if N%2==1:
#                 ans = ans * current_product

#             current_product = current_product * current_product
#             N = N // 2
#         return ans

class Solution:

  def myPow(self, x: float, n: int) -> float:
    def solve(base: float, power: int) -> float:
      if power == 0:
        return 1.0

      if power % 2 == 0:
        return solve(base * base, power // 2)

      return base * solve(base * base, (power - 1) // 2)

    N = n
    if N < 0:
      x = 1 / x
      N = -N

    return solve(x, N)
        
        