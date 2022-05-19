class Solution {
public:
    bool isHappy(int n) {
        while(true)
        {
        long long x,result=0;
        x:
        while(n!=0)
        {
        int res = n%10;
        n=n/10;
        result = result+res*res ;
        
        }
        
        if(1<=result && result <=9)
        {
            if(result==1 ||result==7)
            {
                return true;
            }
            else{
                return false;
            }
        }
       else n=result;
        }
    }        
};