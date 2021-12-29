// N번째 큰 수
// 10개의 원소를 가진 배열 A가 주어진다.
// 3번째로 큰 수 출력
// 2021-12-27

#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main()
{

	int T;
	cin >> T;

	for (int i = 0; i < T; i++) {
		vector<int> v;
		for (int j = 0; j < 10; j++) {
			int x;
			cin >> x;

			v.push_back(x);
		}
		sort(v.begin(), v.end(), less<>());
		for (int j = 0; j < 2; j++) {
			v.pop_back();
		}
		cout << v.back() << endl;
	}

	return 0;
}