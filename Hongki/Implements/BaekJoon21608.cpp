#include <iostream>
#include <vector>
using namespace std;

int locations[21][21];
int dir[4][2] = { {-1, 0}, {0, 1}, {1, 0}, {0, -1} };
int n, total, answer = 0;

vector<vector<int>> v;

bool inBound(int y, int x) {
	return y >= 1 && y <= n && x >= 1 && x <= n;
}


//우선순위 : 좋아하는 사람 명수 -> 주변 빈 자리 갯수 -> 행이 작은 거 -> 열이 작은 거
void findLocation(int idx) {
	int standard = v[idx][0]; //기준
	int y = 0, x = 0, likeCnt = 0, cnt = 0, likeCntStandard = -1, cntStandard = -1;

	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= n; j++) {//자리 2중
			likeCnt = 0, cnt = 0;
			if (locations[i][j] != 0) continue; //자리 있으면 x

			for (int k = 0; k < 4; k++) {
				int my = i + dir[k][0];
				int mx = j + dir[k][1];

				if (!inBound(my, mx)) continue;// 배열 벗어나면?
				if (locations[my][mx] == 0) cnt++;//빈 자리 갯수 + 1
				else {
					for (int l = 1; l <= 4; l++) {
						if (locations[my][mx] == v[idx][l]) { //만일 좋아하는 사람?
							likeCnt++;
						}
					}
				}
			}

			if (likeCnt > likeCntStandard ||
				likeCnt == likeCntStandard && cnt > cntStandard) {
				y = i, x = j;
				likeCntStandard = likeCnt;
				cntStandard = cnt;
			}
		}
	}
	if (y == 0 && x == 0) {
		for (int i = 1; i <= n; i++) {
			for (int j = 1; j <= n; j++) {
				if (locations[i][j] == 0) {
					locations[i][j] = standard;
					return;
				}
			}
		}
	}
	locations[y][x] = standard;
}

int main() {
	ios::sync_with_stdio(0); cin.tie(0);
	int a, b, c, d, e;
	cin >> n;

	total = n * n;
	for (int i = 0; i < total; i++) {
		cin >> a >> b >> c >> d >> e;
		v.push_back({ a,b,c,d,e });
	}

	for (int i = 0; i < total; i++) findLocation(i);

	int cnt = 0, standard = 0;
	for (int i = 1; i <= n; i++) {
		for (int j = 1; j <= n; j++) {
			for (int m = 0; m < total; m++) {
				if (locations[i][j] != v[m][0]) continue;
				else standard = v[m][0];
				cnt = 0;

				for (int k = 0; k < 4; k++) {
					int my = i + dir[k][0];
					int mx = j + dir[k][1];

					if (!inBound(my, mx)) continue;
					for (int l = 1; l <= 4; l++) {
						if (locations[my][mx] == v[m][l]) cnt++;
					}
				}
			}
			if (cnt == 1) answer += 1;
			else if (cnt == 2) answer += 10;
			else if (cnt == 3) answer += 100;
			else if (cnt == 4) answer += 1000;
		}
	}
	cout << answer;
}
