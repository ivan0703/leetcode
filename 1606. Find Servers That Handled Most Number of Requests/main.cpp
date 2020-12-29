#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

class Solution {
public:
    vector<int> busiestServers(int k, vector<int>& arrival, vector<int>& load) {
        int N = arrival.size();
        vector<int> job_cnt(k, 0);
        vector<int> busy_end_time(k,0);
        for(int i=0; i<N; i++) {
            for(int j=0, serv = i % k; j<k; j++, serv++) {
                serv %= k;
                if(busy_end_time[serv] <= arrival[i]) {
                    busy_end_time[serv] = arrival[i] + load[i];
                    job_cnt[serv]++;
                    break;
                }
            }
        }

        auto cmp = [](pair<int,int> left, pair<int,int> right) { return left.first < right.first; };
        std::priority_queue<pair<int,int>, std::vector<pair<int,int>>, decltype(cmp)> pq(cmp);
        for(int i=0; i<job_cnt.size(); i++) {
            pq.push(make_pair(job_cnt[i],i));
        }
        
        int max = 0;
        vector<int> ret;
        while(!pq.empty()) {
            if(pq.top().first >= max) {
                max = pq.top().first;
                ret.push_back(pq.top().second);
                pq.pop();
                continue;
            }
            break;
        }
                
        return ret;
    }
};

int main()
{
    Solution sol;

    // 4
    // [1,3,4,5,10,12]
    // [11,9,3,1,9,12]
    int k = 4;
    vector<int> arrival = {1,3,4,5,10,12};
    vector<int> load = {11,9,3,1,9,12};
    vector<int> ret = sol.busiestServers(k, arrival, load);

    for(int n : ret) {
        cout<<n<<",";
    }
    cout<<endl;

    return 0;
}