#include <iostream>
#include <vector>
#include <algorithm>
#define fastio cin.tie(0)->sync_with_stdio(0);
using namespace std;

int crptSize, alphaCnt;
vector<char> alphaStore;
bool visited[15];

void dfs(string answer, int idx, int even, int odd) {
	if (answer.length() == crptSize) {
		if (even >= 2 && odd >= 1) cout << answer << '\n';
		return;
	}
	for (int i = idx; i < alphaCnt; i++) {
		if (!visited[i]) {
			visited[i] = true;
			if (alphaStore[i] == 'a' || alphaStore[i] == 'e' || alphaStore[i] == 'i' || alphaStore[i] == 'o' || alphaStore[i] == 'u') {
				dfs(answer + alphaStore[i], idx + 1, even, odd + 1);
			}
			else dfs(answer + alphaStore[i], idx + 1, even + 1, odd);
			for (int j = i + 1; j < alphaCnt; j++) visited[j] = false;
		}
	}
}

int main() {
	fastio;
	cin >> crptSize >> alphaCnt;
	for (int i = 0; i < alphaCnt; i++) {
		char c; cin >> c;
		alphaStore.push_back(c);
	}
	sort(alphaStore.begin(), alphaStore.end());
	dfs("", 0, 0, 0);
}