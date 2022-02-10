# 풀이보고 Combinations, permutations 대체하는 방안 찾아보기

# Combinations & asterik 이용
import sys
from itertools import combinations

n = int(input())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

team_stat = [sum(i) + sum(j) for i, j in zip(graph, zip(*graph))]
all_team_stat = sum(team_stat)//2

answer = 40001
for n in combinations(team_stat, n//2):
    answer = min(answer, abs(all_team_stat - sum(n)))

print(answer)


# # Combintations
# from itertools import combinations
# n = int(input())
# data = [list(map(int, input().split())) for _ in range(n)]

# def make_team_case(team):
#     return list(combinations(team, n//2))

# def sum_of_data(sum, check_rest, t):
#     for i, j in combinations(t, 2):
#         sum += (data[i-1][j-1] + data[j-1][i-1])
#         check_rest[i], check_rest[j] = True, True
#     return sum

# def check_min_case(t):
#     first_sum, second_sum, check_rest = 0, 0, [False] * (n+1)

#     first_sum = sum_of_data(first_sum, check_rest, t)    
#     rest_t = [i for i in range(n+1) if i != 0 and check_rest[i] == False]
#     second_sum = sum_of_data(second_sum, check_rest, rest_t)

#     return abs(second_sum - first_sum)

# def main():
#     # Make team case
#     team = [i for i in range(1, n+1)]
#     team_case = make_team_case(team)

#     # Check min case
#     result = 40000
#     for t in team_case:
#         result = min(result, check_min_case(t))
    
#     print(result)

# if __name__ == "__main__":
#     main()