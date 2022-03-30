#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

struct pos{
  int y, x;
};
bool visited[100][100];
int dir[4][2] = { {-1, 0}, {0, 1}, {1, 0}, {0, -1} };
int number_of_area;
int max_size_of_one_area;

bool inBound(int y, int x, int m, int n) {
    return y >= 0 && y < m && x >= 0 && x < n;
}

void bfs(int m, int n, int l, int k, vector<vector<int>>& picture){
    int area = 1;
    queue<pos> q;
    q.push({l, k});
    ++number_of_area;
    
    while (!q.empty()) {
        int y = q.front().y;
        int x = q.front().x;
        visited[y][x] = true;
        q.pop();
        
        for (int i = 0; i < 4; i++) {
            int my = y + dir[i][0];
            int mx = x + dir[i][1];
            
            if (!inBound(my, mx, m, n)) continue;
            if (!visited[my][mx] && (picture[y][x] == picture[my][mx])) {
                visited[my][mx] = true;
                q.push({my, mx});
                ++area;
            }
        }
    }
    max_size_of_one_area = max(max_size_of_one_area, area);
}

vector<int> solution(int m, int n, vector<vector<int>> picture) {
    number_of_area = 0;
    max_size_of_one_area = 0;
    
    for (int i = 0; i < 100; i++) {
        for (int j = 0; j < 100; j++) {
            visited[i][j] = false;
        }
    }
    
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (!visited[i][j] && picture[i][j] != 0) bfs(m, n, i, j, picture);
        }
    }
    
    vector<int> answer(2);
    answer[0] = number_of_area;
    answer[1] = max_size_of_one_area;
    return answer;
}
