// YonseiTOTO
// 전체 과목 수N, 마일리지m, 신청한 사람 수 Pi, 수강인원 Li
// 주어진 마일리지로 최대로 들을 수 있는 과목 수 출력
// 2021-12-27

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> arr;

int main()
{
	int N, m;
	int answer = 0;
	cin >> N >> m; // 전체 과목 수, 마일리지 입력

	for (int i = 0; i < N; i++) {
		vector<int> v;

		int p, l;
		cin >> p >> l; // 신청 수, 수강인원

		for (int j = 0; j < p; j++) {
			int x;
			cin >> x;

			v.push_back(x);
		}
		sort(v.begin(), v.end(), greater<>()); // 다른 사람들 마일리지 내림차순
		if (p > l) {
			while (v.size() > l) {
				v.pop_back();
			}
			arr.push_back(v.back());
		}
		else if (p == l) {
			arr.push_back(v.back());
		}
		else
			arr.push_back(1);
	}

	sort(arr.begin(), arr.end(), less<>()); // 사용 마일리지 오름차순

	for (int i = 0; i < arr.size(); i++) {
		if (m >= arr[i]) {
			m -= arr[i];
			answer++;
		}
	}
	cout << answer;

	return 0;
}