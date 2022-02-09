class Solution {
public:
    int fourSumCount(vector<int>& nums1, vector<int>& nums2, vector<int>& nums3, vector<int>& nums4) {
        int answer = 0;
        unordered_map<int, int> m;
        
        for (auto i : nums1) {
            for (auto j : nums2) m[i + j]++;
        }
        
        for (auto k : nums3) {
            for (auto l : nums4) answer += m[-k - l];
        }
        
        return answer;
    }
};
