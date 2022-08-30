class Solution:
    def fib(self, n: int) -> int:
        if n==0:
            return 0
        if n==1:
            return 1
        # dp = [-1]*(n+1)
        prev2 =0
        prev =1
        for i in range(2,n+1):
            curi=prev2+prev
            prev2 = prev
            prev = curi
        return prev
        