#include <iostream>
#include <cstdint>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	ios::sync_with_stdio(0); cin.tie(0); cout.tie(0);
	uint64_t topingCnt, dowPrice, topingPrice, dowCalorie;
	cin >> topingCnt >> dowPrice >> topingPrice >> dowCalorie;

	vector<uint64_t> topingStore(topingCnt);

	for (int i = 0; i < topingCnt; i++) cin >> topingStore[i];
	sort(topingStore.rbegin(), topingStore.rend());

	for (int i = 0; i < topingCnt; i++) {
		if (dowCalorie / dowPrice <= topingStore[i] / topingPrice) {
			dowCalorie += topingStore[i];
			dowPrice += topingPrice;
		}
		else break;
	}
	cout << dowCalorie / dowPrice;
}