#User function Template for python3


#Complete this function
class Solution:
    def floorSqrt(self, x): 
        
    #Your code here
        t=1
        while(t*t<=x):
            t+=1
        
    
        return t-1
        # low=0
        # high=x
        # def binary_c(low,high,x):
        #     if(low<=high):
        #         mid=low+(high-low)//2
                
        #         if(mid*mid==x):
        #             return mid
        #         elif(mid*mid>x):
        #             return binart_c(0,mid-1,x)
        #         else:
        #             return binary_c(mid+1,high,x)

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math



def main():
        T=int(input())
        while(T>0):
            
            x=int(input())
            
            print(Solution().floorSqrt(x))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends