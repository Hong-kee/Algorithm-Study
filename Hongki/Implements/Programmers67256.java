import java.util.*;

class Solution {
    private static int[] left = {4, 1};
    private static int[] right = {4, 3};
    
    public String solution(int[] numbers, String hand) {
        String answer = "";
        
        for (int i = 0; i < numbers.length; i++) {
            if (numbers[i] == 0) numbers[i] = 11;   
            answer += isHand(numbers[i], hand);
        }
        return answer;
    }

    public String isHand(int number, String hand) {
        int y = number / 3;
        if (number % 3 != 0) ++y;
        
        int x = number % 3;
        if (x == 0) x = 3;
        
        //중앙
        if (number == 2 || number == 5 || number == 8 || number == 11) {
            if (Math.abs(left[0] - y) + Math.abs(left[1] - x) > Math.abs(right[0] - y) + Math.abs(right[1] - x)) {
                right[0] = y; right[1] = x;
                return "R";
                
            } else if (Math.abs(left[0] - y) + Math.abs(left[1] - x) < Math.abs(right[0] - y) + Math.abs(right[1] - x)) {
                left[0] = y; left[1] = x;
                return "L";
                
            } else {
                if (hand.equals("left")) {
                    left[0] = y; left[1] = x;
                    return "L";
                    
                } else {
                    right[0] = y; right[1] = x;
                    return "R";
                }
            }
        }
        
        //왼손
        if (number == 1 || number == 4 || number == 7 || number == 10) {
            left[0] = y; left[1] = x;
            return "L";
        }
        //오른손
        else {
            right[0] = y; right[1] = x;
            return "R";
        }
    }
}
