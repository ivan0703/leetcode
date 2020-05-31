#include <iostream>
#include <map>
#include <string>
#include <vector>

using namespace std;

class RangeModule {
    // true: left, false: right
    map<int, bool> ranges;
public:
    void traceRange() {
        for(auto p : ranges) {
            if(p.second)
                cout<<"  ["<<p.first<<",";
            else 
                cout<<p.first<<")"<<endl;
        }
    }

    RangeModule() {
    }
    
    void addRange(int left, int right) {
        ranges[left] = true;
        ranges[right] = false;
        auto lo = ranges.lower_bound(left);
        auto up = ranges.upper_bound(right);

        if(lo!=ranges.begin() && prev(lo)->second) {
            lo = prev(lo);
        }
        if(up==ranges.end() || (up!=ranges.end() && up->second)) {
            up = prev(up);
        }
        ranges.erase(next(lo), up);
    }
    
    bool queryRange(int left, int right) {
        if(ranges.empty())
            return false;
        
        bool lo = false, res = false;
        for(auto it = ranges.begin(); it!=ranges.end(); it++) {
            if(it->first<=left && it->second) {
                lo = true;
            } else if(it->first>=right) {
                if(!it->second && lo) {
                    res = true;
                    break;
                }
                break;
            } else {
                lo = false;
            }
        }
        return res;
    }
    
    void removeRange(int left, int right) {
        if(ranges.empty())
            return;
        
        auto lo = ranges.lower_bound(left);
        if(lo->first==left) {
            if(!lo->second & lo!=ranges.end())
                lo = next(lo);
        } else {
            if(lo!=ranges.begin() && prev(lo)->second) {
                ranges[left] = false;
            }
        }
        
        auto up = ranges.upper_bound(right);
        if(up!=ranges.end() && !up->second) {
            ranges[right] = true;
            up = prev(up);
        }
        if(up==ranges.end() || lo->first < up->first) {
            ranges.erase(lo,up);
        }
    }
};

using namespace std;

int main()
{
    RangeModule obj;

    // ["RangeModule","addRange","removeRange","queryRange","queryRange","queryRange"]
    // [[],[10,20],[14,16],[10,14],[13,15],[16,17]]
    // obj.addRange(10,20);
    // obj.removeRange(14,16);
    // cout<<obj.queryRange(10,14)<<endl;
    // cout<<obj.queryRange(13,15)<<endl;
    // cout<<obj.queryRange(16,17)<<endl;

    // ["RangeModule","addRange","removeRange","removeRange","addRange","removeRange","addRange","queryRange","queryRange","queryRange"]
    // [[],[6,8],[7,8],[8,9],[8,9],[1,3],[1,8],[2,4],[2,9],[4,6]]
    // obj.addRange(6,8);
    // obj.removeRange(7,8);
    // obj.removeRange(8,9);
    // obj.addRange(8,9);
    // obj.removeRange(1,3);
    // obj.addRange(1,8);
    // cout<<obj.queryRange(2,4)<<endl;
    // cout<<obj.queryRange(2,9)<<endl;
    // cout<<obj.queryRange(4,6)<<endl;

    vector<string> cmds = {"RangeModule","queryRange","addRange","removeRange","queryRange","addRange","addRange","removeRange","removeRange","addRange","addRange","removeRange","queryRange","addRange","addRange","addRange","removeRange","addRange","addRange","queryRange","removeRange","addRange","queryRange","addRange","queryRange","queryRange","removeRange","queryRange","removeRange","addRange","queryRange","removeRange","addRange","removeRange","removeRange","addRange","removeRange","queryRange","removeRange","removeRange","removeRange","addRange","queryRange","addRange","addRange","addRange","queryRange","removeRange","addRange","addRange","removeRange","removeRange","queryRange","removeRange","queryRange","queryRange","queryRange","removeRange","queryRange","addRange","queryRange","queryRange","addRange","queryRange","removeRange","removeRange","addRange","addRange","addRange","addRange","queryRange","removeRange","addRange","removeRange","queryRange","queryRange","removeRange","removeRange","removeRange","addRange","removeRange","queryRange","queryRange","queryRange","removeRange","queryRange","removeRange","queryRange","addRange","queryRange","queryRange"};
    vector<vector<int>> range = {
        {},{17,34},{37,97},{4,85},{19,87},{19,78},{47,59},{56,71},{6,7},{43,95},{42,61},{36,95},{2,63},{30,89},{10,90},{30,99},{47,72},{17,92},{3,68},{2,83},{79,95},{5,16},{17,74},{38,98},{26,69},{82,84},{37,63},{23,89},{19,69},{8,33},{47,93},{18,71},{4,26},{27,75},{32,90},{3,71},{14,68},{39,99},{34,35},{6,57},{36,51},{64,76},{44,48},{12,50},{19,34},{28,55},{15,60},{29,85},{25,59},{30,44},{16,26},{53,86},{72,95},{27,64},{75,78},{60,78},{41,100},{8,49},{84,91},{43,90},{42,66},{83,88},{7,61},{87,100},{19,29},{10,77},{46,80},{75,95},{81,94},{17,95},{19,32},{21,46},{14,82},{35,47},{57,96},{37,94},{23,99},{68,77},{47,100},{23,81},{28,56},{30,46},{82,97},{36,43},{84,91},{47,88},{11,93},{10,77},{7,33},{23,43},{19,69}
    };

    for(int i=0; i<cmds.size(); i++) {
        cout<<"===> i="<<i<<endl;
        if(cmds[i] == "RangeModule") {
            // nothing
        } else if(cmds[i] == "addRange") {
            obj.addRange(range[i][0], range[i][1]);
            cout<<"addRange("<<range[i][0]<<","<<range[i][1]<<"):"<<endl;
            obj.traceRange();
        } else if(cmds[i] == "removeRange") {
            obj.removeRange(range[i][0], range[i][1]);
            cout<<"removeRange("<<range[i][0]<<","<<range[i][1]<<"):"<<endl;
            obj.traceRange();
        } else if(cmds[i] == "queryRange") {
            cout<<obj.queryRange(range[i][0], range[i][1])<<endl;
        } 
    }
 
    return 0;
}
