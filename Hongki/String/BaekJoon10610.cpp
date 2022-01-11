#include <iostream>
#include <string>
#include <algorithm>
#define fastio cin.tie(0) -> ios::sync_with_stdio(0)
using namespace std;

int main() {
	fastio;
	int answer = 0;
	string number; cin >> number;
	sort(number.rbegin(), number.rend());

	//예외처리
	if (number.back() != '0') cout << -1;
	else {
		for (int i = 0; i < number.length(); i++) {
			answer += number[i] - '0';
		}

		if (answer % 3 != 0) cout << -1;
		else cout << number;
	}
}