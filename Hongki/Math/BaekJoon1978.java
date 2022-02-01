import java.io.*;
import java.util.*;

public class Main {

    static BufferedReader br;
    static StringTokenizer st;
    static int n, answer = 0;

    public static void main(String[] args) throws IOException {

        br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());

        for (int i = 0; i < n; i++) {
            answer += checkPrime(Integer.parseInt(st.nextToken()));
        }
        System.out.print(answer);
    }

    static int checkPrime(int num) {
        if (num == 1) return 0;
        for (int i = 2; i <= num / 2; i++) {
            if (num % i == 0) return 0;
        }
        return 1;
    }
}
