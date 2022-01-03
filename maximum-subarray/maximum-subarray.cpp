class Solution {
public:
    
//     Kadane's method= algorithm for sub array sum. In this method we just iterate once over the given input array.
    int maxSubArray(vector<int>& nums) {
         int max_sum=INT_MIN;
        int cur=0;
        for(auto x:nums)
        {
            if(cur<0) cur = 0;
            cur +=x;
            max_sum = max(max_sum,cur);
        }
        return max_sum;
    }
};