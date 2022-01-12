#include <iostream>
#include <string>
#include <algorithm>
#define fastio cin.tie(0)->ios::sync_with_stdio(0)
using namespace std;

int gcd(int maxNum, int minNum) {
	int c;

	while (minNum != 0) {
		c = maxNum % minNum;
		maxNum = minNum;
		minNum = c;
	}
	return maxNum;
}

int main() {
	fastio;
	string ratio; cin >> ratio;
	int idx = 0, maxNum, minNum;
	bool isBig = true;

	for (int i = 0; i < ratio.length(); i++) {
		if (ratio[i] == ':') break;
		++idx;
	}

	if (stoi(ratio.substr(0, idx)) < stoi(ratio.substr(idx + 1, ratio.length()))) isBig = false;

	maxNum = max(stoi(ratio.substr(0, idx)), stoi(ratio.substr(idx + 1, ratio.length())));
	minNum = min(stoi(ratio.substr(0, idx)), stoi(ratio.substr(idx + 1, ratio.length())));

	int getGcd = gcd(maxNum, minNum);
	if (isBig)
		cout << maxNum / getGcd << ':' << minNum / getGcd;
	else
		cout << minNum / getGcd << ':' << maxNum / getGcd;

}
