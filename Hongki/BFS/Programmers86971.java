import java.util.*;
import java.io.*;

class Solution {
    static boolean[][] connections;
    static int answer = 987654321;
    
    public int solution(int n, int[][] wires) {
        
        connections = new boolean[n + 1][n + 1];
        
        for (int i = 0; i < wires.length; i++) {
            connections[wires[i][0]][wires[i][1]] = true;
            connections[wires[i][1]][wires[i][0]] = true;
        }
        
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                if (connections[i][j]) {
                    connections[i][j] = false;
                    connections[j][i] = false;
                    
                    bfs(n, i);
                    
                    connections[i][j] = true;
                    connections[j][i] = true;
                }
            }
        }
        
        return answer;
    }
    
    public void bfs(int n, int start) {
        boolean[] visited = new boolean[n + 1];
        Queue<Integer> q = new LinkedList<>();
        
        q.offer(start);
        visited[start] = true;
        
        int cnt = 1;
        
        while (!q.isEmpty()) {
            int cur = q.poll();
            
            for (int i = 1; i <= n; i++) {
                if (connections[cur][i] && !visited[i]) {
                    visited[i] = true;
                    q.offer(i);
                    cnt++;
                }
            }
        }
        
        answer = Math.min(answer, Math.abs(2 * cnt - n));
    }
}
