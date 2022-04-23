#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>
#define INF -987654321
using namespace std;

int board[20][20];
int boardTemp[20][20];
int dir[4][2] = { {-1, 0},{0, 1},{1, 0},{0, -1} };
int n, m, answer = 0;//board 크기, 일반 블록 색상, 점수
bool visited[20][20];

vector<pair<pair<int, int>, pair<int, int>>> v;

//경계
bool inBound(int y, int x) {
	return y >= 0 && y < n && x >= 0 && x < n;
}

//방문 초기화
void initVisited() {
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) visited[i][j] = false;
	}
}

//블록 찾기 로직
void findBlocks(int y, int x) {
	queue<pair<int, int>> q;

	//블록 갯수, 기준 블록, 기준y, 기준x
	int myCnt = 1, commonBlock = 0, rainbowBlock = 0, standardBlock = board[y][x], standardY = y, standardX =x;
	q.push(make_pair(y, x));

	while (!q.empty()) {
		int y = q.front().first;
		int x = q.front().second;
		visited[y][x] = true;
		q.pop();

		for (int i = 0; i < 4; i++) {
			int my = y + dir[i][0];
			int mx = x + dir[i][1];

			if (!inBound(my, mx) || visited[my][mx]) continue;
			
			//일반 블록 -> 일반 블록 / 무지개 블록 -> 일반 블록
			if (board[y][x] == standardBlock && board[my][mx] == standardBlock || board[y][x] == 0 && board[my][mx] == standardBlock) {
				visited[my][mx] = true;
				q.push(make_pair(my, mx));
				myCnt++;
				commonBlock++;
				//크기를 구하기 위해
				if (standardY < my) standardY = my;
				if (standardX < mx) standardX = mx;
			}
			//일반 블록 -> 무지개 블록 / 무지개 블록 -> 무지개 블록
			else if (board[y][x] == standardBlock && board[my][mx] == 0 || board[y][x] == 0 && board[my][mx] == 0) {
				visited[my][mx] = true;
				q.push(make_pair(my, mx));
				myCnt++;
				commonBlock++;
				rainbowBlock++;
				//크기를 구하기 위해
				if (standardY < my) standardY = my;
				if (standardX < mx) standardX = mx;
			}
		}
	}
	//만일 블록 갯수 >= 2? 벡터에 넣기(블록 갯수, 무지개 블록), (행의 크기, 열의 크기), (기준 블록y, 기준 블록x)
	if (myCnt >= 2 && commonBlock >= 1) v.push_back(make_pair((make_pair(myCnt, rainbowBlock)), make_pair(y, x)));
	
	//무지개 블록 방문 해제
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if (board[i][j] == 0) visited[i][j] = false;
		}
	}
}

//점수 계산 로직 + 블럭 없애기
void calculateAnswer() {
	initVisited();//방문 초기화
	sort(v.rbegin(), v.rend());
	answer += v.front().first.first * v.front().first.first;

	//기준 블록 좌표 + 값
	int y = v.front().second.first;
	int x = v.front().second.second;
	int standardBlock = board[y][x];

	vector<pair<int, int>> locations;
	locations.push_back(make_pair(y, x));
	queue<pair<int, int>> q;
	q.push(make_pair(y, x));

	while (!q.empty()) {
		y = q.front().first;
		x = q.front().second;
		visited[y][x] = true;

		q.pop();

		for (int i = 0; i < 4; i++) {
			int my = y + dir[i][0];
			int mx = x + dir[i][1];

			if (!inBound(my, mx) || visited[my][mx]) continue;

			//일반 블록 -> 일반 블록 / 일반 블록 -> 무지개 블록 / 무지개 블록 -> 일반 블록 / 무지개 블록 -> 무지개 블록
			if (board[y][x] == standardBlock && board[my][mx] == standardBlock || board[y][x] == standardBlock && board[my][mx] == 0 || 
				board[y][x] == 0 && board[my][mx] == standardBlock || board[y][x] == 0 && board[my][mx] == 0) {
				visited[my][mx] = true;
				q.push(make_pair(my, mx));
				locations.push_back(make_pair(my, mx));
			}
		}
	}

	for (int i = 0; i < locations.size(); i++) board[locations[i].first][locations[i].second] = INF;
}

//중력 적용하기
void applyGravity() {
	
	//아래서 부터
	for (int i = 0; i < n; i++) {
		for (int j = n - 2; j >= 0; j--) {
			//계속 내려갈 수 있는가?
			bool isDown = true;
			//선택된 곳이 빈 칸 or 검은색? x
			if (board[j][i] == INF || board[j][i] == -1) continue;
			int mj = j;
			while (isDown) {
				//바닥에 닿을 경우?
				if (mj == n - 1) break;
				//빈 칸이 아닐 경우?
				if (board[mj + 1][i] != INF) isDown = false;
				else {
					board[mj + 1][i] = board[mj][i];
					board[mj][i] = INF;
				}
				mj++;
			}
		}
	}
}

//90도 반시계
void reverseClock() {
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) boardTemp[i][j] = board[j][n - i - 1];
		
	}

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) board[i][j] = boardTemp[i][j];
	}
}

int main() {
	ios::sync_with_stdio(0); cin.tie(0);
	bool isOver = false;
	cin >> n >> m;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) cin >> board[i][j];
	}

	while (1) {
		//블록 찾기
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				//방문하지 않고, 검은색, 무지개, 빈 칸이 아니어야 한다.
				if (!visited[i][j] && board[i][j] != -1 && board[i][j] != 0 && board[i][j] != INF) findBlocks(i, j);
			}
		}
		//게임 실행을 안했다면? 탈출
		if (v.empty()) break;
		//점수 계산 + 블럭 없애기
		calculateAnswer();
		//중력 주기
		applyGravity();
		//90도 반시계 회전
		reverseClock();
		//중력 주기
		applyGravity();
		//벡터, 방문 초기화
		v.clear();
		initVisited();
	}
	cout << answer;
}
