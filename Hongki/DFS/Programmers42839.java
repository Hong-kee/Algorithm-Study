import java.util.*;
import java.io.*;

class Solution {
    static boolean[] visited;
    static Set<String> valueSet = new HashSet<>();
    
    public int solution(String numbers) {
        visited = new boolean[numbers.length()];
        
        dfs("", numbers);
        
        return valueSet.size();
    }
    
    public void dfs(String value, String numbers) {
        if (!value.equals("")) {
            if (value.charAt(0) != '0') {
                if (checkPrime(Integer.parseInt(value))) {
                    valueSet.add(value);
                }
            }
        }
        
        for (int i = 0; i < numbers.length(); i++) {
            if (!visited[i]) {
                visited[i] = true;
                dfs(value + numbers.charAt(i), numbers);
                visited[i] = false;
            }
        }
    }
    
    public boolean checkPrime(int number) {
        if (number == 1) return false;
        
        for (int i = 2; i <= Math.sqrt(number); i++) {
            if (number % i == 0) return false;
        }
        
        return true;
    }
}
