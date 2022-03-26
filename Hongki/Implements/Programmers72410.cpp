#include <string>
#include <vector>
#include <iostream>
using namespace std;

string solution(string new_id) {
    string answer = "";
    int zero_cnt = 0;
    //1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
    for (int i = 0; i < new_id.length(); i++) new_id[i] = tolower(new_id[i]);
    
    //2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
    for (int i = 0; i < new_id.length(); i++) {
        if (new_id[i] >= 'a' && new_id[i] <= 'z' || new_id[i] >= '0' && new_id[i] <= '9' 
            || new_id[i] == '-' || new_id[i] == '_' || new_id[i] == '.') answer += new_id[i];
    }
    
    //3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
    new_id.clear();
    for (int i = 0; i < answer.length(); i++) {
        if (answer[i] == '.') zero_cnt++;
        else if (answer[i] != '.' && zero_cnt >= 1) {
            new_id += '.';
            new_id += answer[i];
            zero_cnt = 0;
        }
        else new_id += answer[i];
    }
    
    //4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
    if (!new_id.empty() && new_id[new_id.length() - 1] == '.') new_id.pop_back();
    if (!new_id.empty() &&new_id[0] == '.') new_id.erase(0, 1);
    
    //5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
    if (new_id.empty()) new_id += 'a';
    
    //6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
    //만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
    if (new_id.length() >= 16) new_id.erase(15, new_id.length());
    if (new_id[new_id.length() - 1] == '.') new_id.pop_back();
    
    //7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
    while (new_id.length() <= 2) {
        new_id += new_id.back();
    }
    //출력 체크
    cout<<new_id;
    
    return new_id;
}
