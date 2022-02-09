class Solution {
public:
    int alpha[26] = {0, };
    char findTheDifference(string s, string t) {
        int idx = 0;

        for (int i = 0; i < s.length(); i++) ++alpha[s[i] - 'a'];
        for (int i = 0; i < t.length(); i++) {
            --alpha[t[i] - 'a'];
            if (alpha[t[i] - 'a'] < 0) {
                idx = i; break;
            }
        }
        return t[idx];
    }
};
