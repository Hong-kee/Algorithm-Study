#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;
    int idx = 0;

    while (1) {
        for (int i = idx; i < progresses.size(); i++) {//더한다.
            progresses[i] += speeds[i];
        }
        int cnt = 0;//갯수 초기화

        for (int i = idx; i < progresses.size(); i++) {
            if (progresses[idx] >= 100) { //검사
                idx = i+1;
                cnt++;
            }
            else {
                break;
            }
        }
        if (cnt > 0) {//갯수 넣기
            answer.push_back(cnt);
            if (idx == progresses.size()) {
                break;
            }
        }
    }
    return answer;
}
