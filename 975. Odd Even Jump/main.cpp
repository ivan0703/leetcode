#include <iostream>
#include <vector>
#include <map>

using namespace std;

class Solution {
public:
    int oddEvenJumps(vector<int>& A) {
        int N = A.size();
        int res = 0;
        map<int,int> m;
        vector<bool> dp_odd(N, false);
        vector<bool> dp_even(N, false);

        m[A[N-1]] = N-1;
        dp_odd[A.size()-1] = true;
        dp_even[A.size()-1] = true;
        res++;

        for(int i = A.size()-2; i>=0; i--) {
            auto it_low = m.lower_bound(A[i]);
            auto it_up  = m.upper_bound(A[i]);
            if(it_low != m.end()) {
                dp_odd[i] = dp_even[it_low->second];
            }
            if(it_up != m.begin()) {
                dp_even[i] = dp_odd[(--it_up)->second];
            }

            if(dp_odd[i]) res++;
            m[A[i]] = i;
        }

        return res;
    }
};

int main()
{
    vector<int> v1 = {10,13,12,14,15};
    vector<int> v2 = {2,3,1,1,4};
    vector<int> v3 = {5,1,3,4,2};

    Solution sol;
    cout<<sol.oddEvenJumps(v1)<<endl;
    cout<<sol.oddEvenJumps(v2)<<endl;
    cout<<sol.oddEvenJumps(v3)<<endl;
    return 0;
}