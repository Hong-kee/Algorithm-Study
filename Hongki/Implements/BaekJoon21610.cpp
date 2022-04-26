#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int baskets[51][51];//맵
int dir[8][2] = { {0, -1}, {-1, -1}, {-1, 0}, {-1, 1}, {0, 1}, {1, 1}, {1, 0}, {1, -1} };//방향
int n, m;//맵의 크기, 이동 횟수
bool checkCloud[51][51];

struct info {
	int direction, moveCnt;
};
struct pos {
	int y, x;
};
vector<info> moveInfo;//이동 정보
queue<pos> locations;//y, x값

//경계
bool inBound(int y, int x) {
	return y >= 1 && y <= n && x >= 1 && x <= n;
}

//구름 이동
void moveCloud(int direction, int moveCnt) {
	int locationsSize = locations.size();
	for (int i = 0; i < locationsSize; i++) {
		int y = locations.front().y + (dir[direction][0] * moveCnt) % n;
		int x = locations.front().x + (dir[direction][1] * moveCnt) % n;
		locations.pop();

		//y처리
		if (y == 0) y = n;
		else if (y < 0) y += n;
		else if (y > n) y %= n;

		//x처리
		if (x == 0) x = n;
		else if (x < 0) x += n;
		else if (x > n) x %= n;

		locations.push({ y, x });
	}
}

//비 내리기
void rainDrop() {
	int locationsSize = locations.size();
	queue<int> rain;

	for (int i = 0; i < locationsSize; i++) {
		int y = locations.front().y;
		int x = locations.front().x;
		locations.pop();

		baskets[y][x]++;
		locations.push({ y, x });
	}

	for (int i = 0; i < locationsSize; i++) {
		int y = locations.front().y;
		int x = locations.front().x;
		int cnt = 0;
		locations.pop();

		for (int j = 1; j < 8; j += 2) {
			int my = y + dir[j][0];
			int mx = x + dir[j][1];

			if (!inBound(my, mx)) continue;
			if (baskets[my][mx] <= 0) continue;
			cnt++;
		}
		rain.push(cnt);
		locations.push({ y, x });
	}

	for (int i = 0; i < locationsSize; i++) {
		int y = locations.front().y;
		int x = locations.front().x;
		int rainCnt = rain.front();
		locations.pop();
		rain.pop();

		baskets[y][x] += rainCnt;
		locations.push({ y, x });
	}
}

//구름 생기기
void makeCloud() {
	int locationSize = locations.size();
	for (int i = 0; i < locationSize; i++) {
		int y = locations.front().y;
		int x = locations.front().x;
		locations.pop();

		checkCloud[y][x] = true;
	}

	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= n; j++) {
			if (!checkCloud[i][j] && baskets[i][j] >= 2) {
				locations.push({ i, j });
				baskets[i][j] -= 2;
			}
		}
	}
	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= n; j++) checkCloud[i][j] = false;
	}
}

//정답
int totalRain() {
	int answer = 0;
	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= n; j++) answer += baskets[i][j];
	}
	return answer;
}

int main() {
	ios::sync_with_stdio(0); cin.tie(0);
	cin >> n >> m;
	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= n; j++) cin >> baskets[i][j];
	}

	for (int i = 1; i <= m; i++) {
		int direction, moveCnt; cin >> direction >> moveCnt;
		moveInfo.push_back({ direction, moveCnt });
	}
	//초기 세팅
	for (int i = n - 1; i <= n; i++) {
		for (int j = 1; j <= 2; j++) locations.push({ i, j });
	}

	//m번 동안 돈다.
	for (int i = 0; i < moveInfo.size(); i++) {
		//구름이동
		moveCloud(moveInfo[i].direction - 1, moveInfo[i].moveCnt);
		//비 내리기
		rainDrop();
		//구름 생기기
		makeCloud();
	}

	cout << totalRain();
}
