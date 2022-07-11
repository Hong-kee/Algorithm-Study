class Solution {
    private static int answer = 0;
    
    public int solution(int n, int[][] computers) {
        for (int i = 0; i < n; i++) {
            if (computers[i][i] == 1 && dfs(i, computers)) answer++;
        }
        return answer;
    }
    
    public static boolean dfs(int idx, int[][] computers) {
        if (computers[idx][idx] == 0) return false;
        computers[idx][idx] = 0;
        
        for (int i = 0; i < computers[idx].length; i++) {
            if (computers[idx][i] == 1) dfs(i, computers);
        }
        
        return true;
    }
}
