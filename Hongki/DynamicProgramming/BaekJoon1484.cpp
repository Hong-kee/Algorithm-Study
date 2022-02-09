#include <iostream>
#include <vector>
#define fastio cin.tie(0)->sync_with_stdio(0)
using namespace std;

int main() {
	fastio;
	int s = 1, e = 1, n; cin >> n;
	vector<int> kgStore;

	while (1) {
		if (e * e - s * s < n) ++e;
		else if (e * e - s * s > n) ++s;
		else {
			kgStore.push_back(e);
			++e;
		}
		if (e >= n) break;
	}
	if (kgStore.empty()) {
		cout << -1;
		return 0;
	}
	for (int i = 0; i < kgStore.size(); i++) cout << kgStore[i] << '\n';
}
