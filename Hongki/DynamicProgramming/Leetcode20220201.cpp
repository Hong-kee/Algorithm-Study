class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int answer = -1, maxPrice = prices[prices.size() - 1];
        
        for (int i = prices.size() - 1; i > 0; --i) {
            if (maxPrice < prices[i - 1]) maxPrice = prices[i - 1];
            else if (maxPrice > prices[i - 1]) answer = max(answer, maxPrice - prices[i - 1]);
        }
        if (answer == -1) return 0;
        return answer;
    }
};
