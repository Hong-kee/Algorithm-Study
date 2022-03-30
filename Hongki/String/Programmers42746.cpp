#include <string>
#include <vector>
#include <algorithm>
using namespace std;

bool cmp(string s1, string s2) {
    return s1 + s2 > s2 + s1;
}

string solution(vector<int> numbers) {
    string answer = "";
    vector<string> numberStore;
    for (int i = 0; i < numbers.size(); i++) numberStore.push_back(to_string(numbers[i]));
    sort(numberStore.begin(), numberStore.end(), cmp);
    for (int i = 0; i < numberStore.size(); i++) answer.append(numberStore[i]);
    if (answer[0] == '0') answer = "0";
    return answer;
}
