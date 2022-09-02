class Solution:

    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        dic =[-1 for i in range(n)]
        dic[0],dic[1] =1 , 2
        return self.helper(n-1,dic)
    def helper(self,n,dic):
        if dic[n]<0:
            dic[n] = self.helper(n-1,dic)+self.helper(n-2,dic)
        return dic[n]
        
#       APproach 3(constant space)
        # if n==1:f n==1
        #     return 1
        # a,b =1,2
        # for i in range(2,n):
        #     tmp = b
        #     b = a+b
        #     a= tmp
        # return b
            
        
        
#         Apprach 2
        # if n==1:
        #     return 1
        # res = [0 for i in range(n)]
        # res[0]=1
        # res[1]=2
        # for i in range(2,n):
        #     res[i] = res[i-1]+res[i-2]
        # return res[-1]
        
        #Approach1
        
        # if n==1:
        #     return 1
        # if n==2:
        #     return 2
        # return self.climbStairs(n-1)+self.climbStairs(n-2)
        