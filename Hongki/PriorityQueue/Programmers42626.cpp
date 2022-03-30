#include <string>
#include <vector>
#include <queue>
using namespace std;

int solution(vector<int> scoville, int K) {
    priority_queue<int, vector<int>, greater<int>> pq;
    int answer = 0;
    
    for (int i = 0; i < scoville.size(); i++) pq.push(scoville[i]);

    while (pq.size() >= 2 && pq.top() < K) {
        int spicyLevel = pq.top();
        pq.pop();
        spicyLevel += pq.top() * 2;
        pq.pop();
        pq.push(spicyLevel);
        answer++;
    }
    if (pq.top() >= K) return answer;
    else return -1;
}
