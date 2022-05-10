class Solution {
public:
    int countOdds(int low, int high) {
        int res;
        res=(high-low)/2;
        if(low%2!=0 || high%2!=0)
        {
            res=res+1;
        }
        return res;
    }
};

// 1)loop from low to high
// 2)increment low
// 3)if(low%2!=0) then count incremnet
//   4) in else condition pass


// 6-10=3
// 3-9=5
//     2-6=3