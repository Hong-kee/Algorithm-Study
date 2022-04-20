#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>
using namespace std;

struct litter {
	int A;
	int B;
	int C;
};

bool visited[201][201][201];

int main() {
	ios::sync_with_stdio(0); cin.tie(0);

	int A, B, C;
	cin >> A >> B >> C;

	queue<litter> q;
	vector<int> answer;
	q.push({ 0, 0, C });

	while (!q.empty()) {
		int a = q.front().A;
		int b = q.front().B;
		int c = q.front().C;

		q.pop();

		if (visited[a][b][c]) continue;
		visited[a][b][c] = true;

		if (a == 0) answer.push_back(c);
		//A->B
		if (a > B - b) q.push({ a - (B - b), B, c });
		else q.push({ 0, a + b, c });

		//A->C
		if (a > C - c) q.push({ a - (C - c), b, C });
		else q.push({ 0, b, a + c });

		//B->A
		if (b > A - a) q.push({ A, b - (A - a), c });
		else q.push({ a + b, 0, c });

		//B->C
		if (b > C - c) q.push({ a, b - (C - c), C });
		else q.push({ a, 0, b + c });

		//C->A
		if (c > A - a) q.push({ A, b, c - (A - a) });
		else q.push({ a + c, b, 0 });

		//C->B
		if (c > B - b) q.push({ a, B, c - (B - b) });
		else q.push({ a, b + c, 0 });
	}
	sort(answer.begin(), answer.end());
	answer.erase(unique(answer.begin(), answer.end()), answer.end());
	for (int i = 0; i < answer.size(); i++) cout << answer[i] << ' ';
}
