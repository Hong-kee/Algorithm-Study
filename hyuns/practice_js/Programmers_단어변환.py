from collections import Counter
def bfs(index, target, words): 
    visit = [False] * len(words)
    visit[index] = True
    q = [[words[index], 1, visit]]
    answer = len(words)
    while q:
        now, ans, visit = q[0]
        q = q[1:]
        if now == target:
            answer = min(answer, ans)
        else:
            for i in range(len(words)):
                if visit[i] == True:
                    continue
                if len(Counter(words[i]) - Counter(now)) == 1:
                    visit[i] = True
                    q.append([words[i], ans+1, visit])
        
    return answer

def solution(begin, target, words):
    answer = len(words)
    if not target in words:
        return 0
    
    for index in range(len(words)):
        if len(Counter(words[index]) - Counter(begin)) == 1:
            answer = min(answer, bfs(index, target, words))
            
    return answer

begin = "cat"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]

print(solution(begin, target, words))