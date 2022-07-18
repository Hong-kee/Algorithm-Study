import java.util.*;
import java.io.*;

class Solution {
    
    public int[] solution(int n, String[] words) {
        int[] answer = new int[2];
        int personNumber = 1, rotation = 1;
        Map<String, Boolean> wordMap = new HashMap<>();
        wordMap.put(words[0], true);
        
        for (int i = 1; i < words.length; i++) {
            
            if (i % n == 0) ++rotation;
            if (i % n == 0) personNumber = 1;
            else ++personNumber;
            
            if (words[i - 1].charAt(words[i - 1].length() - 1) != words[i].charAt(0)) {
                answer[0] = personNumber;
                answer[1] = rotation;
                
                return answer;
            }
            if (!wordMap.containsKey(words[i])) wordMap.put(words[i], true);
            else {
                answer[0] = personNumber;
                answer[1] = rotation;
                
                return answer;
            }
        }
        return answer;
    }
}
