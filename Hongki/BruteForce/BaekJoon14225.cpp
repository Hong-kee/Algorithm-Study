#include <iostream>
#include <vector>
#include <algorithm>
#define fastio cin.tie(0)->ios::sync_with_stdio(0)
using namespace std;

vector<int> numberStore, plusStore;
bool visited[20];
int numCnt, num;

int minNum() {
	if (plusStore[0] != 1) return 1;
	for (int i = 0; i < plusStore.size(); i++) {
		if (i == plusStore.size() - 1) return plusStore[plusStore.size() - 1] + 1;
		else if (plusStore[i] == plusStore[i + 1]) continue;
		else if (plusStore[i] + 1 != plusStore[i + 1]) return plusStore[i] + 1;
	}
}

void dfs(int idx, int number) {
	visited[idx] = true;
	for (int i = idx; i < numCnt; i++) {
		if (!visited[i]) {
			visited[i] = true;
			plusStore.push_back(number + numberStore[i]);
			dfs(i, number + numberStore[i]);
			visited[i] = false;
		}
	}
}

int main() {
	fastio;
	cin >> numCnt;
	for (int i = 0; i < numCnt; i++) {
		cin >> num;
		numberStore.push_back(num);
		plusStore.push_back(num);
	}
	for (int i = 0; i < numberStore.size(); i++) dfs(i, numberStore[i]);
	sort(plusStore.begin(), plusStore.end());
	cout << minNum();
}