import java.util.*;
import java.io.*;

class Solution {
    static boolean[] visited = new boolean[3];
    
    static char[] operand = {'*', '+', '-'};
    static List<Character> selectedOperand = new ArrayList<>();
    static List<String> tempList = new LinkedList<>();
    
    static long answer = -1;
    
    public long solution(String expression) {
        String tempNumber = "";
        List<String> numberList = new LinkedList<>();
        
        for (int i = 0; i < expression.length(); i++) {
            if (expression.charAt(i) == '*' || expression.charAt(i) == '+' || 
               expression.charAt(i) == '-') {
                
                tempList.add(tempNumber);
                tempList.add(expression.charAt(i) + "");
                
                tempNumber = "";
                
            } else {
                tempNumber += expression.charAt(i) + "";
            }
        }
        
        if (!tempNumber.equals("")) tempList.add(tempNumber);
        
        orderOperand(0, expression, numberList);
        
        return answer;
    }
    
    static void orderOperand(int count, String expression, List<String> numberList) {
        if (count == 3) {
            calculateValue(expression, numberList);
            return;
        }
        
        for (int i = 0; i < 3; i++) {
            if (!visited[i]) {
                visited[i] = true;
                selectedOperand.add((Character)operand[i]);
                orderOperand(count + 1, expression, numberList);
                selectedOperand.remove(selectedOperand.size() - 1);
                visited[i] = false;
            }
        }
    }
    
    static void calculateValue(String expression, List<String> numberList) {
        numberList.clear();
        for (String s : tempList) numberList.add(s);

        long tempAnswer = 0;
        
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < numberList.size(); j++) {
                
                for (String s : numberList) System.out.print(s + " ");
                System.out.println();
                
                if (numberList.get(j).equals(selectedOperand.get(i) + "") && selectedOperand.get(i) == '*') { // *의 순번이고 *이라면 ?
                    
                    long calculating = Long.parseLong(numberList.get(j - 1)) * Long.parseLong(numberList.get(j + 1));
                    
                    for (int k = 0; k < 3; k++) numberList.remove(j - 1);
                    
                    numberList.add(j - 1, Long.toString(calculating));
                    j--;
                }
                else if (numberList.get(j).equals(selectedOperand.get(i) + "") && selectedOperand.get(i) == '+') { 
                    
                    long calculating = Long.parseLong(numberList.get(j - 1)) + Long.parseLong(numberList.get(j + 1));
                    
                    for (int k = 0; k < 3; k++) numberList.remove(j - 1);
                    
                    numberList.add(j - 1, Long.toString(calculating));
                    j--;
                }
                else if (numberList.get(j).equals(selectedOperand.get(i) + "") && selectedOperand.get(i) == '-') { 
                
                    long calculating = Long.parseLong(numberList.get(j - 1)) - Long.parseLong(numberList.get(j + 1));
                    
                    for (int k = 0; k < 3; k++) numberList.remove(j - 1);
                    
                    numberList.add(j - 1, Long.toString(calculating));
                    j--;
                }
            }
        }
        
        if (numberList.size() == 1) {
            answer = Math.max(answer, Math.abs(Long.parseLong(numberList.get(0))));
        }
        else {
            if (numberList.get(1).equals("*")) tempAnswer =  Math.abs(Long.parseLong(numberList.get(0)) * Long.parseLong(numberList.get(2)));
            else if (numberList.get(1).equals("+")) tempAnswer =  Math.abs(Long.parseLong(numberList.get(0)) + Long.parseLong(numberList.get(2)));
            else tempAnswer =  Math.abs(Long.parseLong(numberList.get(0)) - Long.parseLong(numberList.get(2)));
            
            answer = Math.max(answer, tempAnswer);
        }
    }
}
