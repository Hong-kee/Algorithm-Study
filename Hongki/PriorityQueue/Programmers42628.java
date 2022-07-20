import java.util.*;
import java.io.*;

class Solution {
    static PriorityQueue<Integer> pq = new PriorityQueue<>();
    static int[] answer = {0, 0};
    
    public int[] solution(String[] operations) {
        
        for (String str : operations) {
            String[] operation = str.split(" ");
            
            if (!pq.isEmpty()) System.out.println(pq.peek());
            
            if (operation[0].equals("I")) pq.add(Integer.parseInt(operation[1]));
            else if (operation[0].equals("D") && !pq.isEmpty()) {
                if (operation[1].equals("-1")) pq.poll();
                else {
                    PriorityQueue<Integer> pqTemp = new PriorityQueue<>();
                    
                    while (pq.size() > 1) {
                        pqTemp.add(pq.peek());
                        pq.poll();
                    }
                    pq = pqTemp;
                }
            }
        }

        if (!pq.isEmpty()) {
            answer[0] = pq.peek();
            answer[1] = pq.peek();
            
            pq.poll();
        }

        while (pq.size() >= 2) {
            pq.poll();
        }
        
        if (!pq.isEmpty()) answer[0] = pq.peek();
        
        return answer;
    }
}
