#include <string>
#include <vector>
#include <deque>
using namespace std;

struct info{
  int weight;
  int pos;
};

int solution(int bridge_length, int weight, vector<int> truck_weights) {
    int answer = 0, curWeight = 0;
    deque<info> dq;
    
    while (!(dq.empty() && truck_weights.empty())) {
        if (!dq.empty()) {
            for (int i = 0; i < dq.size(); i++) dq[i].pos++;
            if (dq[0].pos == bridge_length) {
                curWeight -= dq[0].weight;
                dq.pop_front();
            }
        }
        if (curWeight + truck_weights[0] <= weight && !truck_weights.empty()) {
            dq.push_back({truck_weights[0], 0});
            curWeight += truck_weights[0];
            truck_weights.erase(truck_weights.begin(), truck_weights.begin() + 1);
        }
        answer++;
    }
    
    return answer;
}
