#include <iostream>
#include <queue>
#include <algorithm>
using namespace std;

bool map[101][101];
bool visited[101][101];
int dir[4][2] = { {-1, 0}, {0, 1}, {1, 0}, {0, -1} };
int r, c, k, answer = 0;

struct pos {
	int y, x;
};

bool inBound(int y, int x) {
	return y >= 1 && y <= r && x >= 1 && x <= c;
}

void findAnswer(int y, int x) {
	queue<pos> q;
	int tmpAnswer = 1;
	q.push({ y, x });

	while (!q.empty()) {
		int y = q.front().y;
		int x = q.front().x;



		q.pop();

		for (int i = 0; i < 4; i++) {
			int my = y + dir[i][0];
			int mx = x + dir[i][1];

			if (!inBound(my, mx)) continue;
			if (visited[my][mx]) continue;

			if (map[my][mx]) {
				q.push({ my, mx });
				visited[my][mx] = true;
				tmpAnswer++;
			}
		}
	}
	answer = max(answer, tmpAnswer);
}

int main() {
	ios::sync_with_stdio(0); cin.tie(0);
	cin >> r >> c >> k;
	for (int i = 0; i < k; i++) {
		int y, x; cin >> y >> x;
		map[y][x] = true;
	}

	for (int i = 1; i <= r; i++) {
		for (int j = 1; j <= c; j++) {
			if (map[i][j] && !visited[i][j]) {
				visited[i][j] = true;
				findAnswer(i, j);
			}
		}
	}
	cout << answer;
}
