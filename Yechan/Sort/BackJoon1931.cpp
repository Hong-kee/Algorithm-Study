// 회의실 배정
// 회의의 수 N, 시작 시간과 끝나는 시간의 각 회의의 정보가 주어진다.
// 최대 사용할 수 있는 회의의 개수를 출력한다.
// 2021-12-27

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<pair<int, int>> v;

bool compare(pair<int, int> a, pair<int, int> b) // 두번째 순으로 오름차순 정렬
{
	if (a.second == b.second) {
		return a.first < b.first;
	}
	else
		return a.second < b.second;
}

int main()
{
	int N;
	int now = 0;
	int cnt = 0;

	cin >> N;

	for (int i = 0; i < N; i++) {
		int start, end;
		cin >> start >> end;

		v.push_back(make_pair(start, end));
	}
	sort(v.begin(), v.end(), compare);

	for (int i = 0; i < N; i++) { // 현재 시각보다 시작 시각이 크면 카운트
		if (now <= v[i].first) {
			cnt++;
			now = v[i].second;
		}
	}

	cout << cnt << endl;

	return 0;
}