class Solution {
    public int solution(int n, int[] money) {
        int answer = 0;
        int[] dp = new int[n + 1];
        
        //Setting
        dp[0] = 1;
        
        for (int value : money) {
            for (int i = value; i <= n; i++) {
                dp[i] += dp[i - value] % 1000000007;
            }
        }

        return dp[n];
    }
}
