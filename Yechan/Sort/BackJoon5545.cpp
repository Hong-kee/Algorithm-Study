// 최고의 피자
// 토핑 종류의 수 N, 도우의 가격 A, 토핑의 가격 B, 도우의 열량 C, 토핑의 열량 Di가 한 줄에 하나씩 주어진다.
// 1원당 열량이 가장 높은 최고의 피자의 1원당 열량을 출력한다. 소수점 이하는 버리고 정수 값으로 출력한다.
//2021-12-28

#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main()
{
	vector<int> v;

	int N;
	int price_sum, price_topping;
	int cal_sum;
	int no_topping;
	int answer = 0;

	cin >> N;
	cin >> price_sum >> price_topping;
	cin >> cal_sum;

	no_topping = cal_sum * 1.0 / price_sum * 1.0;

	for (int i = 0; i < N; i++) {
		int x;
		cin >> x;

		v.push_back(x);
	}
	sort(v.begin(), v.end(), greater<>());

	for (int i = 0; i < N; i++) {
		cal_sum = cal_sum + v[i];
		price_sum = price_sum + price_topping;
		v[i] = cal_sum * 1.0 / price_sum * 1.0; // 1원당 열량

		answer = max(v[i], answer); // 최대값
	}
	answer = max(answer, no_topping); // 토핑 없는게 최대일 경우

	cout << answer;

	return 0;
}