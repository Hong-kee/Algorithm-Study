import java.io.*;
import java.util.*;

public class Main {

	private static int n, answer = 0;
	private static int[][] schedule;
	
	public static void main(String[] args) throws IOException{

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		n = Integer.parseInt(br.readLine());
		schedule = new int[2][n];
		
		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			schedule[0][i] = Integer.parseInt(st.nextToken());
			schedule[1][i] = Integer.parseInt(st.nextToken());
		}
		
		dfs(0, 0);
		System.out.println(answer);
	}
	
	public static void dfs(int idx, int benefit) {
		if (idx >= n) {
			answer = Math.max(answer, benefit);
			return;
		}
		
		if (idx + schedule[0][idx] <= n) dfs(idx + schedule[0][idx], benefit + schedule[1][idx]);
		else dfs(n, benefit);
		
		dfs(idx + 1, benefit);
	}
}
