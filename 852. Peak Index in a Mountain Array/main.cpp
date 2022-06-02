#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int peakIndexInMountainArray(vector<int>& arr) {
        int left = 0, right = arr.size()-1;
        while(left <= right) {
            int mid = (left + right) / 2;
            if(mid==0 || mid==arr.size()-1)
                break;
            
            if( arr[mid] > arr[mid-1] && arr[mid] > arr[mid+1] ) {
                return mid;
            } else if ( arr[mid] > arr[mid-1] && arr[mid] < arr[mid+1] ) {
                left = mid;
            } else if (arr[mid] < arr[mid-1] && arr[mid] > arr[mid+1]) {
                right = mid;
            } else {
                break;
            }
        }
        
        return -1;
    }
};

int main()
{
    Solution sol;
    vector<int> arr;

    arr = {0,1,0};
    cout<<sol.peakIndexInMountainArray(arr)<<endl;

    arr = {0,2,1,0};
    cout<<sol.peakIndexInMountainArray(arr)<<endl;

    arr = {0,10,5,2};
    cout<<sol.peakIndexInMountainArray(arr)<<endl;

    return 0;
}