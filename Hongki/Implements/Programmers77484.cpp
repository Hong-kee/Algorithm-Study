#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> lottos, vector<int> win_nums) {
    vector<int> answer;
    int cnt = 0, zero_cnt = 0; // 맞은 번호, 0의 갯수

    for (auto num : lottos) {
        if (num == 0) {
            ++zero_cnt;
            continue;
        }
        for (auto win_num : win_nums) {
            if (num == win_num) ++cnt;
        }
    }
    //갯수에 따른 등수 체크
    if (cnt + zero_cnt >= 2) answer.push_back(7 - (cnt + zero_cnt));
    else answer.push_back(6);
    
    if (cnt >= 2) answer.push_back(7 - cnt);
    else answer.push_back(6);
    
    return answer;
}
