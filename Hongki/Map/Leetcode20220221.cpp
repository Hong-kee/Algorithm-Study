class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int cnt = -1, answer = 0;
        unordered_map<int, int> m;
        
        for (int i = 0; i < nums.size(); i++) ++m[nums[i]];
        for (auto iter : m) {
            if (cnt < iter.second) {
                cnt = iter.second;
                answer = iter.first;
            }
        }
        return answer;
    }
};
