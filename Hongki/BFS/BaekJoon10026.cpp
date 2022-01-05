#include <iostream>
#include <string>
#include <queue>
using namespace std;

int dir[4][2] = { {-1, 0}, {0, 1}, {1, 0} ,{0, -1} };
char map[100][100];
bool visited[100][100];
int n, answer = 0;

struct pos {
	int y, x;
};

bool inBound(int y, int x) {
	return y >= 0 && y < n&& x >= 0 && x < n;
}

void initVisited() {
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			visited[i][j] = false;
		}
	}
}

void canDistinct(int y, int x) {
	queue<pos> q;
	q.push({ y, x });
	visited[y][x] = true;

	while (!q.empty()) {
		int y = q.front().y;
		int x = q.front().x;

		q.pop();

		for (int i = 0; i < 4; i++) {
			int my = y + dir[i][0];
			int mx = x + dir[i][1];

			if (!inBound(my, mx)) continue;
			if (!visited[my][mx] && map[y][x] == map[my][mx]) {
				q.push({ my, mx });
				visited[my][mx] = true;
			}
		}
	}
}

void cantDistinct(int y, int x) {
	queue<pos> q;
	q.push({ y, x });
	visited[y][x] = true;

	while (!q.empty()) {
		int y = q.front().y;
		int x = q.front().x;

		q.pop();

		for (int i = 0; i < 4; i++) {
			int my = y + dir[i][0];
			int mx = x + dir[i][1];

			if (!inBound(my, mx)) continue;
			if (!visited[my][mx]) {
				if ((map[y][x] == 'R' || map[y][x] == 'G') && (map[my][mx] == 'R' || map[my][mx] == 'G')) {
					q.push({ my, mx });
					visited[my][mx] = true;
				}
				else if (map[y][x] == 'B' && map[my][mx] == 'B') {
					q.push({ my, mx });
					visited[my][mx] = true;
				}
			}
		}
	}
}

int main() {
	ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);

	cin >> n;
	for (int i = 0; i < n; i++) {
		string s; cin >> s;
		for (int j = 0; j < n; j++) {
			map[i][j] = s[j];
		}
	}

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if (!visited[i][j]) {
				canDistinct(i, j);
				answer++;
			}
		}
	}
	cout << answer << ' ';
	initVisited();
	answer = 0;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if (!visited[i][j]) {
				cantDistinct(i, j);
				answer++;
			}
		}
	}
	cout << answer << ' ';
}