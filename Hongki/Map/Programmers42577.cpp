#include <string>
#include <vector>
#include <unordered_map>
using namespace std;

bool solution(vector<string> phone_book) {
    unordered_map<string, int> mp;

    for (int i = 0; i < phone_book.size(); i++) {
        mp[phone_book[i]] = 1;
    }
    
    for (int i = 0; i < phone_book.size(); i++){
        string number = "";
        for (int j = 0; j < phone_book[i].length(); j++) {
            number += phone_book[i][j];
            if (number != phone_book[i] && mp[number]) return false;
        }
    }
    return true;
}
