#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main() {
	int testCase = 10, num = 1; 
	//cin >> testCase;

	while (testCase--) {
		int buildingCnt; cin >> buildingCnt;
		int answer = 0;
		vector<int> buildings(buildingCnt);

		for (int i = 0; i < buildingCnt; i++) cin >> buildings[i];

		for (int i = 2; i < buildingCnt - 2; i++) {
			int sideBuilding = 0;
			bool isSee = true;

			for (int j = -2; j <= 2; j++) {
				if (j == 0) continue;
				if (buildings[i] < buildings[i + j]) {
					isSee = false;
					break;
				}
				sideBuilding = max(sideBuilding, buildings[i + j]);
			}
			if (isSee) answer += buildings[i] - sideBuilding;
			
		}

		cout << "#" << num++ << " " << answer << '\n';
	}
}
