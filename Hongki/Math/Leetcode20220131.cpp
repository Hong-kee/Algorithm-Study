class Solution {
public:
    int maximumWealth(vector<vector<int>>& accounts) {
        int answer = -1, wealth;
        for (int i = 0; i < accounts.size(); i++) {
            wealth = 0;
            for (int j = 0; j < accounts[i].size(); j++) wealth += accounts[i][j];
            answer = max(answer, wealth);
        }
        return answer;
    }
};
