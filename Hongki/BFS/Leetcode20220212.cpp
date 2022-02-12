class Solution {
    
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        //Exception Logic
        bool isContain = false;
        for (int i = 0; i < wordList.size(); i++) {
            if (endWord == wordList[i]) {
                isContain = true;
                break;
            }
        }
        if (!isContain) return 0;
        //
        
        unordered_set<string> setWord(wordList.begin(), wordList.end());
        queue<pair<string, int>> q; q.push(make_pair(beginWord, 0));
        
        while (!q.empty()) {
            string s = q.front().first;
            int count = q.front().second;
            q.pop();
            
            if (s == endWord) return count + 1;
            setWord.erase(s);
            
            for (int i = 0; i < s.length(); i++) {
                char c = s[i];
                
                for (int j = 0; j < 26; j++) {
                    s[i] = 'a' + j;
                    if (setWord.find(s) != setWord.end()) q.push(make_pair(s, count + 1));
                }
                s[i] = c;
            }
        }
        return 0;
    }
};
