class Solution {
public:
    vector<int> store;
    vector<vector<int>> answer;
    set<vector<int>> s;
    
    bool visited[10];
    
    void dfs(int idx, int count, vector<int>& nums) {
        if (count == nums.size()) {
            s.insert(store);
            return;
        }
        for (int i = 0; i < nums.size(); i++) {
            if (!visited[i]) {
                visited[i] = true;
                store.push_back(nums[i]);
                dfs(i + 1, count + 1, nums);
                visited[i] = false;
                store.pop_back();
            }
        }
    }
    
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        dfs(0, 0, nums);
        for (auto iter = s.begin(); iter != s.end(); iter++) answer.push_back(*iter);
        return answer;
    }
};
