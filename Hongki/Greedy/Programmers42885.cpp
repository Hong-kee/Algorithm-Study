#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> people, int limit) {
    int answer = 0, idx = 0, curWeight = 0;
    sort(people.begin(), people.end());
    
    while (people.size() > idx) {
        curWeight = people.back();people.pop_back();
        if (people[idx] + curWeight <= limit) idx++;
        answer++;
    }
    
    return answer;
}
