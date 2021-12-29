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