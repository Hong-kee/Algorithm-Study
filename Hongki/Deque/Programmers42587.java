import java.util.*;

class Solution {
    public int solution(int[] priorities, int location) {
        int answer = 1, idx = 0;
        Deque<Pair> prioritiess = new ArrayDeque<>();
        
        for (int i = 0; i < priorities.length; i++) 
             prioritiess.add(new Pair(priorities[i], idx++));
        
        while (true) {
            int priority = prioritiess.getFirst().priority;
            int index = prioritiess.getFirst().index;
            boolean isFinish = true;

            for (Pair pair : prioritiess) {
                if (priority < pair.priority) {
                    prioritiess.pollFirst();
                    prioritiess.addLast(new Pair(priority, index));
                    isFinish = false;
                    break;
                }
            }

            if (isFinish && index != location) {
                answer++;
                prioritiess.pollFirst();
            }
            if (isFinish && index == location) {
                return answer;
            }
        }
    }
}

class Pair{
    int priority;
    int index;

    public Pair(int priority, int index) {
        this.priority = priority;
        this.index = index;
    }
}
