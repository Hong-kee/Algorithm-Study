import java.io.*;
import java.util.*;

public class Main {

    static BufferedReader br;
    static StringTokenizer st;
    static int n, answer = 0;
    static int[] soldier;
    static int[] dp;

    public static void main(String[] args) throws IOException{

        br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());
        soldier = new int[n];
        dp = new int[n];

        st = new StringTokenizer(br.readLine());

        for (int i = 0; i < n; i++) soldier[i] = Integer.parseInt(st.nextToken());

        for (int i = 0; i < n; i++) {
            dp[i] = 1;
            for (int j = 0; j < i; j++) {
                if (soldier[i] < soldier[j]) dp[i] = Math.max(dp[i], dp[j] + 1);
            }
        }

        for (int ability : dp) answer = Math.max(answer, ability);
        System.out.println(n - answer);
    }
}
