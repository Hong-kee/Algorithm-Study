#include <string>
#include <vector>
#include <deque>

using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;
    deque<int> dq;
    
    for (int i = 0; i < progresses.size(); i++) dq.push_back(progresses[i]);
    
    while (!dq.empty()) {
        int works = 0;
        
        for (int i = 0; i < dq.size(); i++) dq[i] += speeds[i];
        for (int i = 0; i < dq.size(); i++) {
            if (dq[i] >= 100) works++;
            else break;
        }
        
        for (int i = 0; i < works; i++) {
            dq.pop_front();
            speeds.erase(speeds.begin(), speeds.begin() + 1);
        }
        if (works != 0) answer.push_back(works);
    }
    
    return answer;
}
