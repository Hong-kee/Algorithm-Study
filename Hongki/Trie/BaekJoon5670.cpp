#include <iostream>
#include <string>
#include <vector>
using namespace std;

struct TRIE {
	bool finish;
	int nodeCnt;
	TRIE* node[26];

	TRIE() {
		finish = false;
		for (int i = 0; i < 26; i++) node[i] = NULL;
		nodeCnt = 0;
	}

	~TRIE() {
		for (int i = 0; i < 26; i++) {
			if (node[i]) delete node[i];
		}
	}

	void insert(const string& words, int idx) {
		if (words[idx] == '\0') {
			finish = true;
			return;
		}

		int cur = words[idx] - 'a';
		if (node[cur] == NULL) {
			nodeCnt++;
			node[cur] = new TRIE();
		}
		node[cur]->insert(words, idx + 1);
	}

	double find(const string& words, int idx, int cnt, bool isRoot) {
		if (words[idx] == '\0') return cnt;

		double answer = 0;
		int cur = words[idx] - 'a';
		if (isRoot) {
			answer = node[cur]->find(words, idx + 1, cnt, false); // 자식으로 내려가면서 +1을 한다
		}
		else {
			if (node[cur] != NULL) { // 빈 문자가 아닐 때(유효한 알파벳일 때)
				if (nodeCnt == 1) {
					if (finish) {
						answer = node[cur]->find(words, idx + 1, cnt + 1, false);
					}
					else {
						answer = node[cur]->find(words, idx + 1, cnt, false);
					}
				}
				else {
					answer = node[cur]->find(words, idx + 1, cnt + 1, false);
				}
			}
		}
		return answer;
	}
};

int main() {
	ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);
	int cnt;

	while (cin >> cnt) {
		TRIE* Root = new TRIE();
		vector<string> words(cnt);

		for (int i = 0; i < cnt; i++) {
			cin >> words[i];
			Root->insert(words[i], 0);
		}
		double answer = 0;
		for (int i = 0; i < cnt; i++)
			answer += Root->find(words[i], 0, 1, true);

		cout << fixed;
		cout.precision(2);
		cout << answer / double(cnt) << '\n';

		delete Root;
	}
}