#include <iostream>
#include <vector>
#include <string>
using namespace std;

struct tryGame {
	string tryNum;
	int strike;
	int ball;
};

vector<tryGame> v;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(0);

	string tryNum;
	int testCase, answer = 0, strike, ball;
	cin >> testCase;

	for (int i = 0; i < testCase; i++) {
		cin >> tryNum >> strike >> ball;
		v.push_back({ tryNum, strike, ball });
	}

	for (int i = 123; i <= 987; i++) {
		string number = to_string(i);
		int cnt = 0;

		if (number[0] == number[1] || number[0] == number[2] || number[1] == number[2] || number[0] == '0' ||
			number[1] == '0' || number[2] == '0') continue;

		for (int j = 0; j < v.size(); j++) {
			strike = ball = 0;

			for (int k = 0; k < 3; k++) {
				if (number[k] == v[j].tryNum[k]) strike++;
				if (number[k] == v[j].tryNum[(k + 1) % 3] || number[k] == v[j].tryNum[(k + 2) % 3]) ball++;
			}

			if (v[j].strike == strike && v[j].ball == ball) cnt++;
		}

		if (testCase == cnt) answer++;
	}
	cout << answer;
}
