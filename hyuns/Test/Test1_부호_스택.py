'''

1. 부호

문제.

Input에 부호 (ex. [ "[{()}]", "{}()[]", ... ] 가 들어올 때, 올바른 부호 표현이면 1 아니면 0

올바른 표현 조건.

1)
[] 안에는 [], {}, () 가 들어올 수 있다. 
{} 안에는 {}, () 만 들어올 수 있다.
() 안에는 () 만 들어올 수 있다.

2)
대칭이 맞아야 한다.

3)
닫힌 부호가 들어왔을 때, 가장 나중에 들어온 열린 부호와 맞아야 한다.

'''

data = ["{[()]}", "{[}]", "[{()}]", "[[]}]", "[{}]()"]
result = []

from collections import deque

def check_word(q, check):
    
    if check == "[" and q[-1] == "[":
        return True
    if check == "{" and (q[-1] == "{" or q[-1] == "["):
        return True
    if check == "(":
        return True

    return False

def solution(data):

    for word in data:
        
        q = deque()
        idx = 0

        while idx < len(word):
            
            ch_w = word[idx]

            if ch_w in ["[","{","("]:
                if q and not check_word(q, ch_w):
                    result.append(0)
                    break
                q.append(ch_w)

            else:
                if ch_w == "]":
                    if q.pop() != "[":
                        result.append(0)
                        break
                if ch_w == "}":
                    if q.pop() != "{":
                        result.append(0)
                        break
                if ch_w == ")":
                    if q.pop() != "(":
                        result.append(0)
                        break
            idx += 1
        
        if idx == len(word):
            result.append(1)

    return result

print(solution(data))
    

