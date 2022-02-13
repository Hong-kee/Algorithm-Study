class Solution {
public:
    vector<int> store;
    vector<vector<int>> answer;
    bool visited[10];
    
    void dfs(int idx, vector<int>& nums) {
        answer.push_back(store);
        for (int i = idx; i < nums.size(); i++) {
            if (!visited[i]) {
                visited[i] = true;
                store.push_back(nums[i]);
                dfs(i + 1, nums);
                visited[i] = false;
                store.pop_back();
            }
        }
    }
    
    vector<vector<int>> subsets(vector<int>& nums) {
        dfs(0, nums);
        return answer;
    }
};
