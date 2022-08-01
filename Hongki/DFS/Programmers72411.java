import java.util.*;
import java.io.*;

class Solution {
    static Map<String, Integer> orderMap = new HashMap<>();
    static Set<String> orderSet;
    
    public String[] solution(String[] orders, int[] course) {
        String[] answer;
        List<String> temp = new LinkedList<>();
        
        for (String order : orders) {
            
            for (int value : course) {
                orderSet = new HashSet<>();
                
                combinationOrders(value, 0, 0, order, "");
                
                for (String str : orderSet) {
                    char[] chars = str.toCharArray();
                    Arrays.sort(chars);
                    str = new String(chars);
                    
                    if (orderMap.containsKey(str)) orderMap.put(str, orderMap.get(str) + 1);
                    else orderMap.put(str, 1);
                }
            }
        }
        
        for (int value : course) {
            int count = -1;
            List<String> list = new LinkedList<>();
            
            for (String str : orderMap.keySet()) {
                if (str.length() == value && orderMap.get(str) > 1) {
                    if (count < orderMap.get(str)) {
                        count = orderMap.get(str);
                        list.clear();
                        list.add(str);
                    }
                    else if (count == orderMap.get(str)) list.add(str);
                }
            }
            
            for (String tempStr : list) temp.add(tempStr);
        }
        
        answer = new String[temp.size()];
        int idx = 0;
        
        for (String str : temp) answer[idx++] = str;
        
        Arrays.sort(answer);
        
        return answer;
    }
    
    public static void combinationOrders(int goal, int count, int idx, String order, String tempStr) {
        if (goal == count) {
            orderSet.add(tempStr);
            return;
        }
        
        for (int i = idx; i < order.length(); i++) {
            combinationOrders(goal, count + 1, i + 1, order, tempStr + order.charAt(i));
        }
    }
}
