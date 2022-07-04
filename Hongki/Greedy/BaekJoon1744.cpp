#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
	ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);
	
	int n, answer = 0; cin >> n;
	vector<int> numbers(n);

	for (int i = 0; i < n; i++) cin >> numbers[i];
	sort(numbers.begin(), numbers.end());

	int left = 0, right = n - 1;

	while (left < right) {
		if (numbers[left] < 1 && numbers[left + 1] < 1) {
			answer += numbers[left] * numbers[left + 1];
			left += 2;
		}
		else break;
	}

	while (right > 0) {
		if (numbers[right] > 1 && numbers[right - 1] > 1) {
			answer += numbers[right] * numbers[right - 1];
			right -= 2;
		}
		else break;
	}

	for (int i = left; i <= right; i++) answer += numbers[i];

	cout << answer;
}
