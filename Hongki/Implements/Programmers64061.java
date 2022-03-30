import java.util.*;

class Solution {
    static int answer;
    static Stack<Integer> stack = new Stack<>();
    
    public int solution(int[][] board, int[] moves) {
        for (int i = 0; i < moves.length; i++) moveCrane(board, moves[i] - 1);
        return answer;
    }
    
    static void moveCrane(int[][] board, int col) {
        for (int i = 0; i < board.length; i++) {
            if (board[i][col] != 0) {
                if (!stack.isEmpty()) {
                    if (stack.peek() == board[i][col]) {
                        answer += 2;
                        stack.pop();
                    }
                    else stack.push(board[i][col]);
                }
                else stack.push(board[i][col]);
                board[i][col] = 0;
                break;
            }
        }
    }
}
