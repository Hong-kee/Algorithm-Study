from itertools import combinations
def check_chickenDistance(chicken, home_dir):
    sum_check = 0
    for h_x, h_y in home_dir:
        check = min([abs(h_x - c_x) + abs(h_y - c_y) for c_x, c_y in chicken])
        sum_check += check
    return sum_check

def main():
    global answer
    chicken_comb = combinations(chicken_dir, M)
    answer = min([check_chickenDistance(chicken,home_dir)for chicken in chicken_comb])

if __name__ == "__main__":
    N, M = map(int, input().split())
    chicken_dir, home_dir = [], []
    for i in range(N):
        map_row = list(map(int, input().split()))
        for j in range(N):
            if map_row[j] == 2:
                chicken_dir.append([i, j])
            elif map_row[j] == 1:
                home_dir.append([i, j])
    main()
    print(answer)