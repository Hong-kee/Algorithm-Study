import java.util.*;
import java.io.*;

class Solution {
    static int INF = -987654321;
    
    public int solution(int m, int n, int[][] puddles) {
        int answer = 0;
        
        int[][] map = new int[n + 1][m + 1];
        
        //Setting
        for (int i = 0; i < puddles.length; i++) map[puddles[i][1] - 1][puddles[i][0] - 1] = INF;
        for (int i = 0; i <= m; i++) {
            if (map[0][i] == INF) break;
            else map[0][i] = 1;
        }
        for (int i = 0; i <= n; i++) {
            if (map[i][0] == INF) break;
            else map[i][0] = 1;
        }
        
        
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                if (map[i][j] == INF) continue;
                //오른쪽
                if (map[i - 1][j] != INF) map[i][j] += map[i - 1][j] % 1000000007;
                //아래쪽
                if (map[i][j - 1] != INF) map[i][j] += map[i][j - 1] % 1000000007;
            }
        }
        answer = map[n - 1][m - 1] % 1000000007;
        
        return answer;
    }
}
