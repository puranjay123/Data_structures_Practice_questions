// { Driver Code Starts
#include <bits/stdc++.h>

using namespace std;

 // } Driver Code Ends
// User function template for C++
class Solution {
  public:
    string equilibrium(int *arr, int n) {
        // code here
        int left=0;
        int sum=0;
        int right=0;
        for(int i=0;i<n;i++){
            sum+=arr[i];
        }
        for(int i=0;i<n;i++){
            left+=arr[i];
          
            if(left==right){
                return "YES";
            }
              right=sum-left;
        }
        return "NO";
    }};

// { Driver Code Starts.

int main() {
    int t;
    cin >> t;
    while (t--) {
        int n, i;
        cin >> n;
        int a[n];
        for (i = 0; i < n; i++) {
            cin >> a[i];
        }
        Solution ob;
        auto ans = ob.equilibrium(a, n);
        cout << ans << "\n";
    }
    return 0;
}  // } Driver Code Ends