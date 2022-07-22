import java.util.*;

class Solution {
    static int answer = 0;
    static boolean[] visited;
    
    public int solution(int k, int[][] dungeons) {
        visited = new boolean[dungeons.length];
        
        dfs(k, 0, dungeons);
        
        return answer;
    }
    
    public void dfs(int curFatigue, int cnt, int[][] dungeons) {
        for (int i = 0; i < dungeons.length; i++) {
            if (!visited[i] && curFatigue - dungeons[i][1] >= 0 && curFatigue >= dungeons[i][0]) {
                answer = Math.max(answer, cnt + 1);
                visited[i] = true;
                dfs(curFatigue - dungeons[i][1], cnt + 1, dungeons);
                visited[i] = false;
            }
        }
    }
}
