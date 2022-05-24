#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

bool inBound(int y, int x) {
	return y >= 0 && y < 8 && x >= 0 && x < 8;
}

int main() {
	int testCase = 10, num = 1; 
	//cin >> testCase;

	while (testCase--) {
		char board[8][8];
		int answer = 0;
		int len; cin >> len;

		for (int i = 0; i < 8; i++) {
			for (int j = 0; j < 8; j++) cin >> board[i][j];
		}

		for (int i = 0; i <= 8; i++) {
			for (int j = 0; j <= 8; j++) {
				string str = "";
				bool isOk = true;
				for (int k = 0; k < len; k++) {
					if (!inBound(i, j + k)) {
						isOk = false;
						break;
					}
					str += board[i][j + k];
				}
				if (isOk) {
					for (int k = 0; k < str.length() / 2; k++) {
						if (str[k] != str[len - k - 1]) {
							isOk = false;
							break;
						}
					}
					if (isOk) answer++;
				}

				str = "";
				isOk = true;
				for (int k = 0; k < len; k++) {
					if (!inBound(i + k, j)) {
						isOk = false;
						break;
					}
					str += board[i + k][j];
				}
				if (isOk) {
					for (int k = 0; k < str.length() / 2; k++) {
						if (str[k] != str[len - k - 1]) {
							isOk = false;
							break;
						}
					}
					if (isOk) answer++;
				}
			}
		}

		cout << "#" << num++ << " " << answer << '\n';
	}
}
