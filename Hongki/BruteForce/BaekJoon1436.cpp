#include <iostream>
#include <string>
using namespace std;

int main() {
	ios::sync_with_stdio(0); cin.tie(0);
	int inputNum, cnt = 1; cin >> inputNum;
	string number = "666";
	while (1) {
		if (number.find("666") != string::npos) {
			if (cnt == inputNum) break;
			else ++cnt;
		}
		number = to_string((stoi(number) + 1));
	}
	cout << number;
}