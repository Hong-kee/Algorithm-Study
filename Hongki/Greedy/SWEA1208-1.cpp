#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main() {
	int testCase = 10, num = 1; 
	//cin >> testCase;

	while (testCase--) {
		vector<int> boxes(100);
		int answer = 0, dumpCnt; cin >> dumpCnt;
		dumpCnt += 1;

		for (int i = 0; i < 100; i++) cin >> boxes[i];
		sort(boxes.begin(), boxes.end());

		while (dumpCnt--) {
			sort(boxes.begin(), boxes.end());
			if (boxes[99] - boxes[0] == 0 || boxes[99] - boxes[0] == 1) break;
			boxes[99]--; boxes[0]++;
			answer = boxes[99] - boxes[0];
		}
		cout << "#" << num++ << " " << answer + 2 << '\n';
	}
}
