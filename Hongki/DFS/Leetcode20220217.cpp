class Solution {
public:
    vector<int> store;
    vector<vector<int>> answer;
    set<vector<int>> s;
    
    void dfs(int sum, vector<int>& candidates, int target) {
        if (sum == target) {
            vector<int> v;
            for (int i = 0; i <store.size(); i++) v.push_back(store[i]);
            sort(v.begin(), v.end());
            s.insert(v);
            return;
        }
        for (int i = 0; i < candidates.size(); i++) {
            if (sum + candidates[i] <= target) {
                store.push_back(candidates[i]);
                dfs(sum + candidates[i], candidates, target);
                store.pop_back();
            }
        }
    }
    
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        dfs(0, candidates, target);
        for (auto iter = s.begin(); iter != s.end(); iter++) {
            answer.push_back(*iter);
        }
        return answer;
    }
};
