class Solution {
public:
    int findPairs(vector<int>& nums, int k) {
        int s = 0, e = 0;
        vector<pair<int, int>> v;
        
        sort(nums.begin(), nums.end());
        int sz = nums.size();
        
        while (1) {
          if (e >= sz) break;
          int value = abs(nums[s] - nums[e]);

          if (s == e) ++e;
          else {
             if (value == k) {
                   if (nums[s] >= nums[e]) v.push_back(make_pair(nums[e], nums[s]));
                   else v.push_back(make_pair(nums[s], nums[e]));
                  ++e;
               }
                else if (value > k) ++s;
                else ++e;
            }
        }
        v.erase(unique(v.begin(), v.end()), v.end());
        return v.size();
    }
};
