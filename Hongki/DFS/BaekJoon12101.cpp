#include <iostream>
#include <vector>
#include <string>
using namespace std;

int arr[3] = { 1,2,3 };
int n, k, cnt;
vector<int> v;
string answer = "";

void dfs(int value) {
	if (value == n) {
		cnt++;
		if (cnt == k) {
			for (auto i : v) {
				answer += to_string(i) + "+";
			}
			answer.pop_back();
		}
		return;
	}
	if (value > n) return;
	for (int i = 0; i < 3; i++) {
		v.push_back(arr[i]);
		dfs(value + arr[i]);
		v.pop_back();
	}
}

int main() {
	ios::sync_with_stdio(0); cin.tie(0);
	cin >> n >> k;
	dfs(0);
	if (answer.empty()) answer = "-1";
	cout << answer;
}
