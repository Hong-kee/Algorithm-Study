/*
ÆÑÅä¸®¾ó µÚ 0ÀÇ °¹¼ö (Data : until 2^31 -1)
*/
#include <iostream>
#define fastio cin.tie(0)->ios::sync_with_stdio(0)
using namespace std;

int main() {
	fastio;
	int n, answer = 0; cin >> n;
	while (n >= 5) {
		answer += n / 5;
		n /= 5;
	}
	cout << answer;
}
