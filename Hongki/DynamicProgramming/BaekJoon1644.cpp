#include <iostream>
#include <vector>
#define fastio cin.tie(0)->sync_with_stdio(0)
using namespace std;

int prime[4000001];

int main() {
	fastio;
	int s = 0, e = 0, value = 0, n, answer = 0; cin >> n;
	vector<int> primeStore;

	for (int i = 1; i <= n; i++) prime[i] = i;
	for (int i = 2; i <= n; i++) {
		if (prime[i] == i) {
			for (int j = 2; j * i <= n; j++) {
				if (prime[i * j] == i * j) prime[i * j] = i;
			}
		}
	}

	for (int i = 2; i <= n; i++) {
		if (prime[i] == i) primeStore.push_back(i);
	}

	int sz = primeStore.size();
	
	while (1) {
		if (value >= n) value -= primeStore[s++];
		else if (e == sz) break;
		else value += primeStore[e++];
		if (value == n) ++answer;
	}
	cout << answer;
}
