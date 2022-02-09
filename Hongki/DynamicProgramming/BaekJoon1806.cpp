#include <iostream>
#include <algorithm>
#define fastio cin.tie(0)->sync_with_stdio(0)
using namespace std;

int arr[100001];

int main() {
	fastio;
	int s = 0, e = 0, answer = 987654321, n, sum, value = 0; cin >> n >> sum;
	for (int i = 0; i < n; i++) cin >> arr[i];

	while (1) {
		if (value >= sum) value -= arr[s++];
		else if (e == n) break;
		else value += arr[e++];
		if (value >= sum) answer = min(answer, e - s);
	}
	if (answer == 987654321) answer = 0;
	cout << answer;
}
