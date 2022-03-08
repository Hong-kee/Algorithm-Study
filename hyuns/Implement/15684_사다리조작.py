def check_board(board):

    for j in range(len(board[0])):
        row, col = 0, j
        while row != len(board):
            if col >= 0 and board[row][col] == True:
                col += 1
            elif col > 0 and board[row][col-1] == True:
                col -= 1
            row += 1
        if col != j:
            return False
    return True

def dfs(board, ans, row, col):
    global answer
    
    # 현재 i -> i로 사다리가 이어질 수 있는 지 체크
    if check_board(board):
        answer = min(answer, ans)
        return
    
    # 불필요한 dfs 방지
    if ans >= 3 or answer <= ans:
        return

    for i in range(row, len(board)):
        if i != row: col = 0 # 행 변경 시 열 초기화, dfs를 했을 때 열 값을 가져오기 때문에
        for j in range(col, len(board[i])-1):
            if board[i][j] == False and board[i][j+1] == False: # 현위치, 우방향 체크
                if j > 0 and board[i][j-1] == True: # idx가 0 이상일 경우, 좌방향 체크
                    continue
                board[i][j] = True
                dfs(board, ans+1, i, j+2)
                board[i][j] = False # 백트래킹

if __name__ == "__main__":
    N, M, H = map(int, input().split())
    ladder = []
    answer = 4
    board = [[False] * N for _ in range(H)]
    if M == 0:
        print(0)
        exit(0)

    # 연결된 사다리 True
    for i in range(M):
        x,y = list(map(int, input().split()))
        board[x-1][y-1] = True

    dfs(board, 0,0,0)

    print(answer if answer <= 3 else -1)
