#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>
#define fastio cin.tie(0)->sync_with_stdio(0)
using namespace std;

//index, cnt
typedef pair<int, int> pii;
bool visited[1000];

int bfs(const vector<int>& maze) {
	queue<pii> q;
	q.push({ 0, 0 });

	while (!q.empty()) {
		int idx = q.front().first;
		int cnt = q.front().second;
		visited[idx] = true;
		q.pop();

		for (int i = 1; i <= maze[idx]; i++) {
			int cur = idx + i;
			if (cur == maze.size() - 1) return cnt + 1;
			if (cur > maze.size() - 1) break;
			if (!visited[cur]) {
				visited[cur] = true;
				q.push({ cur, cnt + 1 });
			}
		}
	}
	return -1;
}

int main() {
	fastio;
	int len; cin >> len;
	vector<int> maze(len);
	for (int i = 0; i < len; i++) cin >> maze[i];
	if (len == 1) {
		cout << 0;
		return 0;
	}
	cout << bfs(maze);
}