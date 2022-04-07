class Solution:
    def myPow(self, x, n):

        if n < 0: 
            x = 1/x
            n = abs(n)
        res = 1
        while n:
            if n % 2:
                res = res*x
            x = x*x 
            n = n//2
        return res
