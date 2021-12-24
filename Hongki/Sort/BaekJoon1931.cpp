#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	ios::sync_with_stdio(0); cin.tie(0);

	int N, answer = 1; cin >> N;
	vector<pair<int, int>>v(N);

	for (int i = 0; i < N; i++) cin >> v[i].first >> v[i].second;
	sort(v.begin(), v.end(), greater<>());

	int temp = v[0].first;
	for (int i = 1; i < v.size(); i++) {
		if (temp >= v[i].second) {
			temp = v[i].first;
			answer++;
		}
	}
	cout << answer;
}