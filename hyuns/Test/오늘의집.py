## Problem 3

# {b} {c} d {d} {i} → {b} {c} d {e} {i}
# {c} d d {e} {i} → {c} d d {f} {i}
# d d d {f} {i} → d d d {d} {i}
# d d d {d} {i} → d d d {e} {i}
# d d d {e} {i} → d d d {f} {i}
# d d d {f} {i} → d d d {d} {i}

# 변화 과정 가져가면서 확인하기
def list_toDict(var):
    dict_var = {}
    for v in var:
        dict_var[v[0]] = v[1]

    return dict_var

def solution(tstring, variables):
    answer = ''
    repeat_list = [tstring]
    dict_var = list_toDict(variables)

    while True:

        # for var in variables:
        #     idx = chg_tstring.find(var[0]) # 문자 위치

        #     if idx != -1 and chg_tstring[idx-1] == "{" and chg_tstring[idx+len(var[0])] == "}": # template 문자 확인
        #         tmp_str = "{" + var[0] + "}"
        #         chg_tstring = chg_tstring.replace(tmp_str, var[1])
        tmp_str = ""
        new_str = ""

        for chr in repeat_list[-1]: # 여기 실수 -> 기준 값 변화주지 말기
            if chr == "{" or tmp_str:
                tmp_str += chr
                if tmp_str[-1] == "}": # 여기 실수
                    if tmp_str[1:-1] in dict_var:
                        new_str += dict_var[tmp_str[1:-1]] # 여기 실수
                    else:
                        new_str += tmp_str
                    
                    tmp_str = ""
            else:
                new_str += chr

        answer = new_str
        if answer in repeat_list:
            if answer == repeat_list[-1]:
                answer = repeat_list[-2]
            break
        else:
            repeat_list.append(answer)

    return answer

tstring = "this is {template} {template} is {state}"
#"{a} {b} {c} {d} {i}"
# "this is {template} {template} is {state}"
#"this is {template} {template} is {state}" 
#"this is {template} {template} is {state}"
variables = [["template", "{state}"], ["state", "{template}"]]
#[["b", "{c}"], ["a", "{b}"], ["e", "{f}"], ["h", "i"], ["d", "{e}"], ["f", "{d}"], ["c", "d"]]
#[["template", "{state}"], ["state", "{template}"]]
#[["template", "string"], ["state", "{template}"]] 
#[["template", "string"], ["state", "changed"]]
print(solution(tstring, variables))


## Problem 2

# from collections import Counter
# def solution(call):
#     answer = ""
#     count_call = Counter(call.lower())
#     max_cnt = -1
#     max_chr = []

#     for letter in count_call:

#         if count_call[letter] > max_cnt:
#             max_cnt = count_call[letter]
#             max_chr = []
#             max_chr.append(letter)

#         elif count_call[letter] < max_cnt:
#             continue
        
#         max_chr.append(letter)
    
#     for ltr in call:
#         if not ltr.lower() in max_chr:
#             answer += ltr

#     return answer

# # call = "abcabcdefabc"
# # call = "abxdeydeabz"
# # call = "abcabca"
# call = "ABCabcA"

# print(solution(call))






## Problem 1
# def print_nextDir(lp, rp):
    
#     if (lp == "E" and rp == "S") or (lp == "S" and rp == "W") or (lp == "W" and rp == "N") or (lp == "N" and rp == "E"):
#         return "right"
#     elif (lp == "E" and rp == "N") or (lp == "S" and rp == "E") or (lp == "W" and rp == "S") or (lp == "N" and rp == "W"):
#         return "left"
    
# def read_distance(pth, t):
#     next = ""
#     dir = pth[t]
#     cnt = 0
#     next_dir = -1

#     for i in range(t, len(pth)):
#         if pth[i] != dir:
#             next_dir = i
#             break
#         cnt += 1
    
#     if next_dir != -1:
#         next = print_nextDir(pth[t], pth[next_dir])

#     return cnt, next

# def solution(path):
#     answer = []
#     time = 0
#     # 500m 기준
#     # 진행 방향 left or right
#     # 마지막 방향 조심

#     while time != len(path)-1:
#         # 500m 체크, 다음 방향
#         distance, next_dir = read_distance(path, time)
#         if distance > 5:
#             time += distance - 5
#             distance = 5
        
#         if not next_dir:
#             break
#         else:
#             answer.append(f"Time {time}: Go straight {distance*100}m and turn {next_dir}")
#             time += distance
    
#     return answer
    

# # path = "EEESEEEEEENNNN"
# path = "SSSSSSSSWWWNNN"
# print(solution(path))