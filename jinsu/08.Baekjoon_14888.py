n = int(input())

number = list(map(int, input().split()))

oper = list(map(int, input().split())) # 연산자 갯수

max_value = -float('inf')
min_value = float('inf')
# operator = ['+'*o[0], '-'*o[1], '*'*o[2], '/'*o[3]]
# operator = ''.join(operator).split()

def dfs(index, total, plus, minus, multiply, divide):
    global max_value, min_value 
    if index == n:
        max_value = max(total, max_value)
        min_value = min(total, min_value)
        return
    
    if plus:
        dfs(index+1, total+number[index], plus-1, minus, multiply, divide)
    if minus:
        dfs(index+1, total-number[index], plus, minus-1, multiply, divide)
    if multiply:
        dfs(index+1, total*number[index], plus, minus, multiply-1, divide)
    if divide:
        dfs(index+1, int(total/number[index]), plus, minus, multiply, divide-1)


dfs(1, number[0], oper[0], oper[1], oper[2], oper[3])

print(max_value)
print(min_value)
    













