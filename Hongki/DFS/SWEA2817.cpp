#include <iostream>
#include <algorithm>

using namespace std;

int arr[20];
int answer, cnt, k;

void dfs(int idx, int sum) {
	if (sum > k) return;
	if (sum == k) {
		answer++;
		return;
	}

	for (int i = idx; i < cnt; i++) {
		dfs(i + 1, sum + arr[i]);
	}
}

int main() {
	int testCase, num = 1;
	cin >> testCase;

	while (testCase--) {
		cin >> cnt >> k;
		answer = 0;

		for (int i = 0; i < cnt; i++) cin >> arr[i];

		dfs(0, 0);

		cout << "#" << num++ << " " << answer << '\n';
	}
}
