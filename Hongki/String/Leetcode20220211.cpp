class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        int alpha[26] = {0, };
        int alphaCopy[26] = {0, };
        
        if (s1.length() > s2.length()) return false;
        
        for (int i = 0; i < s1.length(); i++) {
            ++alpha[s1[i] - 'a'];
            ++alphaCopy[s1[i] - 'a'];
        }
        for (int i = 0; i < s2.length(); i++) {
            bool isFinish = true;
            if (i + s1.length() > s2.length()) break;
            
            for (int j = i; j < i + s1.length(); j++) --alpha[s2[j] - 'a'];
            for (int j = 0; j < 26; j++) {
                if (alpha[j] != 0) {
                    isFinish = false;
                    break;
                }
            }
            if (isFinish) return true;
            else {
                for (int j = 0; j < 26; j++) alpha[j] = alphaCopy[j];
            }
        }
        return false;
    }
};
