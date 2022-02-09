class Solution {
public:
    vector<int> findAnagrams(string s, string p) {
        vector<int> answer, sVector(26, 0), pVector(26, 0);
        if (s.length() < p.length()) return answer;
        
        for (int i = 0; i < p.length(); i++) {
            ++pVector[p[i] - 'a'];
            ++sVector[s[i] - 'a'];
        }
        if (sVector == pVector) answer.push_back(0);
        
        for (int i = p.length(); i < s.length(); i++) {
            ++sVector[s[i]-'a'];
            --sVector[s[i - p.size()] - 'a'];
            if (pVector == sVector) answer.push_back(i - p.size() + 1);
        }
        
        return answer;
    }
};
