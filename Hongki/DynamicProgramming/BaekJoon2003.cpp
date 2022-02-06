#include <iostream>
#include <vector>
#define fastio cin.tie(0)->sync_with_stdio(0)
using namespace std;

int main() {
	fastio;
	int s = 0, e = 0, answer = 0, n, m, value = 0; cin >> n >> m;
	vector<int> numStore(n);
	for (int i = 0; i < n; i++) cin >> numStore[i];

	while (1) {
		if (value >= m) value -= numStore[s++];
		else if (e == n) break;
		else value += numStore[e++];
		if (value == m) ++answer;
	}
	cout << answer;
}
