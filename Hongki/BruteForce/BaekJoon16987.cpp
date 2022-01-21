#include <iostream>
#include <vector>
using namespace std;

//내구도, 무게
typedef pair<int, int> pii;

int eggCnt, answer = 0, tempAnswer = 0;

void dfs(int idx, vector<pii> eggInfo) {
	if (idx == eggInfo.size()) {
		tempAnswer = 0;
		for (int i = 0; i < eggCnt; i++) {
			if (eggInfo[i].first <= 0) ++tempAnswer;
		}
		answer = max(answer, tempAnswer);
		return;
	}
	if (eggInfo[idx].first <= 0) dfs(idx + 1, eggInfo);
	else {
		bool isHit = false;
		for (int i = 0; i < eggInfo.size(); i++) {
			if (eggInfo[i].first <= 0 || i == idx) continue;
			eggInfo[idx].first -= eggInfo[i].second;
			eggInfo[i].first -= eggInfo[idx].second;
			isHit = true;
			dfs(idx + 1, eggInfo);
			eggInfo[idx].first += eggInfo[i].second;
			eggInfo[i].first += eggInfo[idx].second;
		}
		if (!isHit) dfs(eggCnt, eggInfo);
	}
}

int main() {
	ios::sync_with_stdio(0); cin.tie(0);
	cin >> eggCnt;
	vector<pii> eggInfo(eggCnt);
	for (int i = 0; i < eggCnt; i++) cin >> eggInfo[i].first >> eggInfo[i].second;
	dfs(0, eggInfo);
	cout << answer;
}