import java.util.*;

class Solution {
    public int[] solution(String[] id_list, String[] report, int k) {
        int[] answer = new int[id_list.length];
        
        Map<String, HashSet<String>> reportMap = new HashMap<>();
        Map<String, Integer> answerMap = new HashMap<>();
        int idx = 0;
        
        for (String id : id_list) {
            reportMap.put(id, new HashSet<>());
            answerMap.put(id, idx++);
        }
        
        for (String name : report) {
            String[] str = name.split(" ");
            reportMap.get(str[1]).add(str[0]);
        }
        
        for (int i = 0; i < id_list.length; i++) {
            HashSet<String> reported = reportMap.get(id_list[i]);
            if (reported.size() >= k) {
                for (String name : reported) answer[answerMap.get(name)]++;
            }
        }

        return answer;
    }
}
