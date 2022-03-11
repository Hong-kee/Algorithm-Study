/**
* brown 10
* yellow 2

* return [col, row]

* brown + yellow의 약수들, if 12?
* 1 2 3 4 6 12
* 가로의 길이가 길어서 뒤에서 부터 탐색
*/
#include <string>
#include <vector>

using namespace std;

vector<int> answer; //정답
int answerBrown, answerYellow;

bool findCarpet(int col, int row, int totalCarpet) {
    int cntB = col * 2 + (row - 2) * 2; //B갯수
    int cntY = (col - 2) * (row - 2); // Y갯수
    
    if (cntB + cntY == totalCarpet && cntB == answerBrown && cntY == answerYellow) return true;
    return false;
}

void searchDivisor(int totalCarpet) {
    for (int i = totalCarpet; i > 0; i--) {
        
         //약수이고 찾았다?
        if (totalCarpet % i == 0 && findCarpet(i, totalCarpet / i, totalCarpet)) {
            answer.push_back(i); answer.push_back(totalCarpet / i);
            return;
        }
    }
}


vector<int> solution(int brown, int yellow) {
    answerBrown = brown, answerYellow = yellow; //저장
    searchDivisor(brown + yellow); //약수 찾기
    return answer;
}
