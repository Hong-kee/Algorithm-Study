# 풀이보고 Combinations, permutations 대체하는 방안 찾아보기

# dfs 이용 풀이 
n = int(input())
data = list(map(int, input().split()))
oper = list(map(int, input().split()))

maximum, minimum = -1e9, 1e9
total = 0

def dfs(idx, total, add, sub, mul, div):

    global maximum, minimum
    if len(data)-1 == idx:
        maximum, minimum = max(maximum, total), min(minimum, total)
        return
    
    if add:
        dfs(idx+1, total+data[idx+1], add-1, sub, mul, div)
    if sub:
        dfs(idx+1, total-data[idx+1], add, sub-1, mul, div)
    if mul:
        dfs(idx+1, total*data[idx+1], add, sub, mul-1, div)
    if div:
        dfs(idx+1, int(total/data[idx+1]), add, sub, mul, div-1)

dfs(0, data[0], oper[0], oper[1], oper[2], oper[3])
print(maximum)
print(minimum)


# Permutation 이용 풀이

# from itertools import permutations
# n = int(input())
# data = list(map(int, input().split()))
# add, sub, mul, div = map(int, input().split())

# def change_op(answer, next, chr):
#     if chr == "a":
#         return answer + next
#     elif chr == "s":
#         return answer - next
#     elif chr == "m":
#         return answer * next
#     else:
#         return -(abs(answer)//abs(next)) if (answer*next) < 0 else (answer//next)

# def calculate(data, op_list):
#     answer = data[0]
#     for i in range(len(op_list)):
#         answer = change_op(answer, data[i+1], op_list[i])
#     return answer

# def main():
#     dic = {"a": add, "s": sub, "m": mul, "d": div}
#     op = [k for k in dic for _ in range(dic[k])]
#     op = list(permutations(op, len(op)))
#     ans_max, ans_min = -1000000001, 1000000001
#     for op_list in op:
#         answer = calculate(data, op_list)
#         ans_max = max(ans_max, answer)
#         ans_min = min(ans_min, answer)
    
#     print(ans_max)
#     print(ans_min)

# if __name__ == "__main__":
#     main()