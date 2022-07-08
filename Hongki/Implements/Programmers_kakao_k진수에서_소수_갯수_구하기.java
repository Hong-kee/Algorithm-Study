import java.util.*;
import java.io.*;

import static java.lang.Math.sqrt;


class Solution {
    
    public int solution(int n, int k) {
        String number = "";
        int answer = 0;

        while (n > 0) {
            number = String.valueOf(n % k) + number;
            n /= k;
        }

        String[] splitNumbers = number.split("0");

        for (String num : splitNumbers) {
            if (num.isEmpty() || num.equals("1")) continue;
            if (isPrime(Long.parseLong(num))) answer++;
        }
        
        return answer;
    }
    
    public static boolean isPrime(Long number) {
        for (int i = 2; i <= sqrt(number); i++) {
            if (number % i == 0) return false;
        }

        return true;
    }
}
