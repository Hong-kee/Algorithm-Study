from itertools import permutations
n = int(input())
data = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

def change_op(answer, next, chr):
    if chr == "a":
        return answer + next
    elif chr == "s":
        return answer - next
    elif chr == "m":
        return answer * next
    else:
        return -(abs(answer)//abs(next)) if (answer*next) < 0 else (answer//next)

def calculate(data, op_list):
    answer = data[0]
    for i in range(len(op_list)):
        answer = change_op(answer, data[i+1], op_list[i])
    return answer

def main():
    dic = {"a": add, "s": sub, "m": mul, "d": div}
    op = [k for k in dic for _ in range(dic[k])]
    op = list(permutations(op, len(op)))
    ans_max, ans_min = -1000000001, 1000000001
    for op_list in op:
        answer = calculate(data, op_list)
        ans_max = max(ans_max, answer)
        ans_min = min(ans_min, answer)
    
    print(ans_max)
    print(ans_min)

if __name__ == "__main__":
    main()