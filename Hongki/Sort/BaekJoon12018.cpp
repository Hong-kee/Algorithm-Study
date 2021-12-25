#include <iostream>
#include <vector>
#include <cstdint>
#include <algorithm>
using namespace std;

int main() {
	ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);

	//과목, 마일리지
	int16_t answer = 0, subject, mileage; cin >> subject >> mileage;
	vector<uint16_t> results;

	while (subject--) {
		int16_t n, m; cin >> n >> m; // 수강인원, 제한인원
		vector<int16_t> mileageStore(n);

		for (int i = 0; i < n; i++) cin >> mileageStore[i];

		// 수강인원 > 제한인원
		if (n > m) {
			sort(mileageStore.rbegin(), mileageStore.rend());
			results.push_back(mileageStore[m - 1]);
		}
		// 수강인원 == 제한인원
		else if (n == m) {
			results.push_back(*min_element(mileageStore.begin(), mileageStore.end()));
		}
		// 수강인원 < 제한인원
		else results.push_back(1);
	}
	//결과 저장소 오름차순
	sort(results.begin(), results.end());

	//마일리지를 최소한으로 쓰되, 최대한의 과목 얻기
	for (int i = 0; i < results.size(); i++) {
		if (mileage - results[i] >= 0) {
			mileage -= results[i]; ++answer;
		}
		else break;
	}
	cout << answer;
}