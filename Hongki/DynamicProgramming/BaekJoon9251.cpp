#include <iostream>
#include <string>
#include <algorithm>
#define fastio cin.tie(0)->sync_with_stdio(0);

using namespace std;

int dp[1001][1001];

int main() {
	fastio;
	string str1, str2; cin >> str1 >> str2;
	int str1Len = str1.length(), str2Len = str2.length();
	for (int i = 0; i < str1Len; i++) dp[i][0] = 0;
	for (int i = 0; i < str2Len; i++) dp[0][i] = 0;

	for (int i = 1; i <= str1Len; i++) {
		for (int j = 1; j <= str2Len; j++) {
			if (str1[i - 1] == str2[j - 1]) dp[i][j] = dp[i - 1][j - 1] + 1;
			else dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
		}
	}
	cout << dp[str1Len][str2Len];
}