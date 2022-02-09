class Solution {
public:
    int addDigits(int num) {
        string s = to_string(num); int answer = 0;
        
        while (s.length() >= 2) {
            for (int i = 0; i < s.length(); i++) answer += s[i] - '0';
            s = to_string(answer); answer = 0;
        }
        return stoi(s);
    }
};
