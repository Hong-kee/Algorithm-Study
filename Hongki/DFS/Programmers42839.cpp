#include <string>
#include <vector>
#include <iostream>
#include <set>

using namespace std;

bool visited[7];
int answer = 0;
set<string> s;

bool isPrime(string tempNumber) {
    if (tempNumber[0] == '0' || tempNumber == "1") return false;
    
    int num = stoi(tempNumber);
    for(int j = 2; j * j <= num; j++) {
        if(num % j == 0) return false;
    }
    return true;
}

void dfs(string tempNumber, string numbers) {
    // cout<<tempNumber<<'\n';
    // for(int i = 0; i < numbers.length(); i++) cout<<visited[i]<<' ';
    // cout<<'\n';
    if (!tempNumber.empty() && isPrime(tempNumber)) s.insert(tempNumber);
    for (int i = 0; i < numbers.length(); i++) {
        if (!visited[i]) {
            visited[i] = true;
            dfs(tempNumber + numbers[i], numbers);
            visited[i] = false;
        }
    }
}

int solution(string numbers) {
    dfs("", numbers);
    return s.size();
}
