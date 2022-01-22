#include <iostream>
#include <queue>
#define fastio cin.tie(0)->sync_with_stdio(0)
using namespace std;

typedef pair<int, int> pii;
int A, B;

int bfs() {
	queue<pii> q;
	q.push({ B, 1 });

	while (!q.empty()) {
		int standard = q.front().first;
		int cnt = q.front().second;
		q.pop();

		if (standard < A) continue;
		else if (standard == A) return cnt;
		else if (standard % 2 == 0) q.push({ standard / 2, cnt + 1 });
		else if ((standard - 1) % 10 == 0) q.push({ (standard - 1) / 10, cnt + 1 });
	}
	return -1;
}

int main() {
	fastio;
	cin >> A >> B;
	cout << bfs();
}
