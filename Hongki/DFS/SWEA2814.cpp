#include <iostream>
#include <algorithm>

using namespace std;

int answer, node, line;
bool arr[11][11];
bool visited[11];

void dfs(int idx, int temp) {
	answer = max(answer, temp);

	for (int i = 1; i <= node; i++) {
		if (arr[idx][i] && !visited[i]) {
			visited[i] = true;
			dfs(i, temp + 1);
			visited[i] = false;
		}
	}
}

int main() {
	ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);
	int testCase, num = 1;
	cin >> testCase;

	while (testCase--) {
		cin >> node >> line;
		answer = 1;

		for (int i = 1; i <= node; i++) visited[i] = false;
		for (int i = 1; i <= node; i++) {
			for (int j = 1; j <= node; j++) arr[i][j] = false;
		}

		for (int i = 1; i <= line; i++) {
			int n, m; cin >> n >> m; 
			arr[n][m] = true;
			arr[m][n] = true;
		}
		
		for (int i = 1; i <= node; i++) {
			visited[i] = true;
			dfs(i, 1);
			visited[i] = false;
		}
		cout << "#" << num++ << " " << answer << '\n';
	}
}
