import java.io.*;
import java.util.*;
import java.awt.*;

public class Main {

	private static int n, answer = 0;
	private static char[][] map;
	private static boolean[][] visited;
	private static int[][] dir = { { -1, 0 }, { 0, 1 }, { 1, 0 }, { 0, -1 } };
	private static Queue<Point> q = new LinkedList<>();
	private static ArrayList arr = new ArrayList();

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		n = Integer.parseInt(br.readLine());
		map = new char[n][n];
		visited = new boolean[n][n];

		for (int i = 0; i < n; i++) {
			String s = br.readLine();
			for (int j = 0; j < s.length(); j++) {
				map[i][j] = s.charAt(j);
			}
		}

		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				if (!visited[i][j] && map[i][j] == '1') {
					bfs(i, j);
					++answer;
				}
			}
		}

		Collections.sort(arr);
		System.out.println(arr.size());
		for (int i = 0; i < arr.size(); i++)
			System.out.println(arr.get(i));
	}

	static void bfs(int i, int j) {
		int cnt = 1;
		q.offer(new Point(i, j));
		visited[i][j] = true;

		while (!q.isEmpty()) {
			Point cur = q.poll();

			for (int k = 0; k < 4; k++) {
				int my = cur.x + dir[k][0];
				int mx = cur.y + dir[k][1];

				if (!inBound(my, mx)) continue;
				if (!visited[my][mx] && map[my][mx] == '1') {
					q.offer(new Point(my, mx));
					visited[my][mx] = true;
					++cnt;
				}
			}
		}
		arr.add(cnt);
	}

	static boolean inBound(int y, int x) {
		if (y >= 0 && y < n && x >= 0 && x < n) return true;
		return false;
	}
}
