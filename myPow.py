class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        
        if n < 0:
            x = 1/x
            n *= -1
        
        if n == 1:
            return x
        elif n == 2:
            return x*x
        else:
            subPow = self.myPow(x, int(n/2))
            if n%2 == 0:
                return subPow*subPow
            else:
                return x*subPow*subPow