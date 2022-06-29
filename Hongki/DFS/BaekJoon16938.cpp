#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int sumDifficult = 0, problemCnt, lowestDifficult, highestDifficult, gapDifficult, answer = 0;
vector<int> problems, store;
bool visited[15];

void solve(int idx, int cnt, int stackDifficult) {
	if (cnt >= 2) {
		if (stackDifficult >= lowestDifficult && stackDifficult <= highestDifficult) {
			if (*max_element(store.begin(), store.end()) - *min_element(store.begin(), store.end()) >= gapDifficult) {
				answer++;
			}
		}
	}
	for (int i = idx; i < problems.size(); i++) {
		if (!visited[i]) {
			store.push_back(problems[i]);
			visited[i] = true;
			solve(i, cnt + 1, stackDifficult + problems[i]);
			store.pop_back();
			visited[i] = false;
		}
	}
}

int main() {
	ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);

	cin >> problemCnt >> lowestDifficult >> highestDifficult >> gapDifficult;

	for (int i = 0; i < problemCnt; i++) {
		int num; cin >> num; problems.push_back(num);
		sumDifficult += problems[i];
	}

	solve(0, 0, 0);

	cout << answer;
}
