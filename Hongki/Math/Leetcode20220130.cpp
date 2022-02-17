class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        int start = nums.size() - (k % nums.size());
      
        for (int i = 0; i < start; i++) nums.push_back(nums[i]);
        nums.erase(nums.begin(), nums.begin() + start);
    }
};
