#include <iostream>
#include <string>
#include <algorithm>
#define fastio cin.tie(0)->sync_with_stdio(0);
using namespace std;

int dp[4002][4002];

int main() {
	fastio;
	string str1, str2; cin >> str1 >> str2;
	int answer = 0;
	for (int i = 0; i < str1.length(); i++) dp[i][0] = 0;
	for (int i = 0; i < str2.length(); i++) dp[0][i] = 0;
	for (int i = 1; i <= str1.length(); i++) {
		for (int j = 1; j <= str2.length(); j++) {
			if (str1[i - 1] == str2[j - 1]) {
				dp[i][j] = dp[i - 1][j - 1] + 1;
				answer = max(answer, dp[i][j]);
			}
		}
	}
	cout << answer;
}