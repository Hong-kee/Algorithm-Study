#include <iostream>
#include <string>
using namespace std;

int main() {
	ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);

	string str, answer, word; getline(cin, str);
	bool isBracket = false;

	for (int i = 0; i < str.length(); i++) {
		if (str[i] == ' ' || !word.empty() && str[i] == '<') {
			for (int j = word.length() - 1; j >= 0; j--) answer += word[j];
			if (str[i] == ' ') answer += ' ';
			if (str[i] == '<') {
				isBracket = true; answer += str[i];
			}
			word.clear();
		}
		else if (str[i] == '<') {
			isBracket = true; answer += str[i];
		}
		else if (str[i] == '>') {
			isBracket = false;
			answer += str[i];
		}
		else if (isBracket) answer += str[i];
		else word += str[i];
	}

	if (!word.empty()) {
		for (int i = word.length() - 1; i >= 0; i--) {
			answer += word[i];
		}
	}
	cout << answer;
}