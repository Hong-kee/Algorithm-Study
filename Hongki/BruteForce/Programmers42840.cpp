#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> answers) {
    vector<int> answer;
    vector<pair<int, int>> ranking;
    
    int giveUp1[5] = { 1, 2, 3, 4, 5 };
    int giveUp2[8] = { 2, 1, 2, 3, 2, 4, 2, 5 };
    int giveUp3[10] = { 3, 3, 1, 1, 2, 2, 4, 4, 5, 5 };
    int answer1 = 0, answer2 = 0, answer3 = 0;
    
    for (int i = 0; i < answers.size(); i++) {
        if (giveUp1[i % 5] == answers[i]) answer1++;
        if (giveUp2[i % 8] == answers[i]) answer2++;
        if (giveUp3[i % 10] == answers[i]) answer3++;
    }
    
    ranking.push_back(make_pair(answer1, 1));
    ranking.push_back(make_pair(answer2, 2));
    ranking.push_back(make_pair(answer3, 3));
    
    sort(ranking.rbegin(), ranking.rend());
    
    answer.push_back(ranking[0].second);
    if (ranking[0].first == ranking[1].first) answer.push_back(ranking[1].second);
    if (ranking[0].first == ranking[2].first) answer.push_back(ranking[2].second);
    
    sort(answer.begin(), answer.end());
    
    return answer;
}
