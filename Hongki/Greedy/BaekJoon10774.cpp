#include <iostream>
#include <vector>
#define fastio cin.tie(0)->ios::sync_with_stdio(0)
using namespace std;

/*
원래는 S < M < L
계산할 땐 L < M < S
*/

int main() {
	fastio;
	int jerseyCnt, members, answer = 0; cin >> jerseyCnt >> members;
	vector<char> jerseySize(1000001);
	bool isSell[1000001] = { false , };

	for (int i = 0; i < jerseyCnt; i++) cin >> jerseySize[i + 1];
	for (int i = 0; i < members; i++) {
		char wantJerseySize; int wantBackNumber;
		cin >> wantJerseySize >> wantBackNumber;

		if (wantJerseySize >= jerseySize[wantBackNumber] && !isSell[wantBackNumber]) {
			++answer;
			isSell[wantBackNumber] = true;
		}
	}
	cout << answer;
}