class Solution {
public:
    double average(vector<int>& salary) {
        double max=INT_MIN;
        double min = INT_MAX;
        for(int i=0;i<salary.size();i++)
        {
            if(max<salary[i])
            {
                max=salary[i];
            }
            if(min>salary[i])
            {
                min=salary[i];
            }
        }
        double ans;
        double sum=0;
        for(int i=0;i<salary.size();i++)
        {
            sum=sum+salary[i];
        }
        sum=sum-max-min;
        double avg=salary.size()-2;
        ans=sum/avg;
        return ans;
    }
};