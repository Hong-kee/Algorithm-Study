import java.util.*;
import java.io.*;

class Solution {
    private static boolean[] visited;
    private static List<String> answer;
    
    public String[] solution(String[][] tickets) {
        visited = new boolean[tickets.length];
        answer = new ArrayList<>();
        
        dfs(0, "ICN", "ICN", tickets);
        
        Collections.sort(answer);
        
        return answer.get(0).split(" ");
    }
    
    public void dfs(int idx, String curPlace, String path, String[][] tickets) {
        if (idx == tickets.length) {
            answer.add(path);
            return;
        }
        
        for (int i = 0; i < tickets.length; i++) {
            if (!visited[i] && curPlace.equals(tickets[i][0])) {
                visited[i] = true;
                dfs(idx + 1, tickets[i][1], path + " " + tickets[i][1], tickets);
                visited[i] = false;
            }
        }
    }
}
