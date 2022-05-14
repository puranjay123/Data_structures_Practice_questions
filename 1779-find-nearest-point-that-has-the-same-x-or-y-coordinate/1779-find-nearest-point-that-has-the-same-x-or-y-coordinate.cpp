class Solution {
public:
    int nearestValidPoint(int x, int y, vector<vector<int>>& points) {
        int min = INT_MAX;
        int result=-1;
        for(int i=0;i<points.size();i++)
        {
            
                if(x==points[i][0] || y==points[i][1])
                {
                   int diff =abs(x-points[i][0])+abs(y-points[i][1]);
                    if(diff<min)
                    {
                        min=diff;
                        result =i;
                    }
                }
            }
        
        return result;
    }
};