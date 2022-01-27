/**
 * 절반만 탐색하면 된다. 왜냐하면 1,2 / 3,4 와 3,4 / 1,2는 같으니까 !
 * 합의 차가 최솟값이 되어야 한다. abs 값으로 출력한다. 0이 나오면 그냥 종료
 *
 */

import java.io.*;
import java.util.*;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static int N, answer = 987654321;
    static int[][] ability;
    static boolean[] visited;

    public static void main(String[] args) throws IOException {

        N = Integer.parseInt(br.readLine());
        ability = new int[N][N];
        visited = new boolean[N];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                ability[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        dfs(0);
        System.out.println(answer);
    }

    static void dfs(int cnt) {
        if (cnt == N) {
            answer = Math.min(answer, diff());
            return;
        }
        visited[cnt] = true;
        dfs(cnt + 1);
        visited[cnt] = false;
        dfs(cnt + 1);
    }

    static int diff() {
        int start = 0, link = 0;

        for (int i = 0; i < N; i++) {
            for (int j = i + 1; j < N; j++) {
                if (visited[i] == visited[j]) {
                    if (visited[i]) start += ability[i][j] + ability[j][i];
                    else link += ability[i][j] + ability[j][i];
                }
            }
        }
        return Math.abs(start - link);
    }
}
