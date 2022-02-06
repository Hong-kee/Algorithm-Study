class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int answer = 2;
        if (nums.size() <= 2) return nums.size();
        for (int i = 2; i < nums.size(); i++) {
            if (nums[i] != nums[answer - 2] || nums[i] != nums[answer - 1]) {
                nums[answer] = nums[i];
                ++answer;
            }
        }
        return answer;
    }
};
