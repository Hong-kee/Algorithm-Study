#include <iostream>
#include <algorithm>
#include <vector>
#define fastio cin.tie(0)->sync_with_stdio(0)
using namespace std;

int main() {
	fastio;
	int s = 0, e = 0, value = 0, answer = 2000000001, n, m; cin >> n >> m;
	vector<int> numStore(n);
	for (int i = 0; i < n; i++) cin >> numStore[i];
	sort(numStore.begin(), numStore.end());

	while (1) {
		if (e == n) break;
		if (numStore[e] - numStore[s] < m) ++e;
		else if (numStore[e] - numStore[s] > m) {
			answer = min(answer, numStore[e] - numStore[s]);
			++s;
		}
		else {
			cout << m;
			return 0;
		}
	}
	cout << answer;
}
