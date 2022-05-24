#include <iostream>
#include <algorithm>
#include <queue>
using namespace std;

int farm[49][49];
bool visited[49][49];
int dir[6][2] = { {1, -1}, {1, 0}, {1, 1},
				 {-1, -1}, {-1, 0}, {-1, 1} };
int answer, len;

struct pos {
	int y, x;
};

void initVisited() {
	for (int i = 0; i < len; i++) {
		for (int j = 0; j < len; j++) visited[i][j] = false;
	}
}

bool inBound(int y, int x) {
	return y >= 0 && y < len && x >= 0 && x < len;
}

void bfsTop(int y, int x) {
	queue<pos> q;
	q.push({ y, x });

	while (!q.empty()) {
		int y = q.front().y;
		int x = q.front().x;
		visited[y][x] = true;
		answer += farm[y][x];
		
		q.pop();

		if (y == len / 2) continue;
		for (int i = 0; i < 3; i++) {
			int my = y + dir[i][0];
			int mx = x + dir[i][1];

			if (!inBound(my, mx)) continue;
			if (visited[my][mx]) continue;
			visited[my][mx] = true;
			q.push({ my,mx });
		}
	}
}

void bfsBottom(int y, int x) {
	queue<pos> q;
	q.push({ y, x });

	while (!q.empty()) {
		int y = q.front().y;
		int x = q.front().x;
		visited[y][x] = true;
		answer += farm[y][x];

		q.pop();

		for (int i = 3; i < 6; i++) {
			int my = y + dir[i][0];
			int mx = x + dir[i][1];

			if (!inBound(my, mx)) continue;
			if (visited[my][mx]) continue;
			visited[my][mx] = true;
			q.push({ my,mx });
		}
	}
}

int main() {
	int testCase, num = 1; cin >> testCase;

	while (testCase--) {
		answer = 0, len; cin >> len;

		for (int i = 0; i < len; i++) {
			string str; cin >> str;
			for (int j = 0; j < len; j++) farm[i][j] = str[j] - '0';
		}

		int topY = 0, topX = len / 2, bottomY = len - 1, bottomX = len / 2;

		if (topY != bottomY) {
			bfsTop(topY, topX);
			bfsBottom(bottomY, bottomX);
			initVisited();
		}
		else {
			answer = farm[topY][topX];
		}
		cout << "#" << num++ << " " << answer << '\n';
	}
}
