class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        unordered_map<int , int> ump;
        int sum = 0, answer = 0;
        
        ump[0] = 1;
        
        for (int i = 0; i < nums.size(); i++) {
            sum += nums[i];
            int key = sum - k;
            
            if (ump.find(key) != ump.end()) answer += ump[key];
            ++ump[sum];
        }
        return answer;
    }
};
