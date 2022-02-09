class Solution {
public:
    int findMaxLength(vector<int>& nums) {
        int value = 0, answer = 0;
        unordered_map<int, int> sum;
        sum[0] = 0; 
        
        for (int i = 1; i <= nums.size(); i++) {
            if (nums[i - 1] == 0) --value;
            else ++value;
            
            if (sum.find(value) != sum.end()) answer = max(answer, i - sum[value]);
            else sum[value] = i;
        }
        
        return answer;
    }
};
