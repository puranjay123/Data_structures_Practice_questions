class Solution {
public:
    int subtractProductAndSum(int n) {
        int sum=0;
        int mul=1,res;
        while(n)
        {
            res=n%10;
            sum=sum+res;
            mul=mul*res;
            n=n/10;
        }
        
        return mul-sum;
    }
};